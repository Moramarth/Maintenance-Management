from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.decorators import group_required
from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.clients.models import ServiceReport
from maintenance_management.estate.models import Building
from maintenance_management.supervisor.filters import AssignmentFilter, initial_query_set_assignments
from maintenance_management.supervisor.forms import AssignForm
from maintenance_management.supervisor.helper_functions import create_assignment_object, report_is_assigned
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


@login_required
@group_required(GroupEnum.supervisor)
def assign_report_to_engineer_or_contractor(request, pk):
    """ Manual assignment of service reports to be handled by engineers or contractors"""
    report = get_object_or_404(ServiceReport, pk=pk)
    form = AssignForm(request.POST or None)
    if form.is_valid():
        user = UserModel.objects.get(pk=form.cleaned_data["assign_to"])
        create_assignment_object(request.user, report, user)
        report_is_assigned(report, user)

        return redirect('report details', pk=report.pk)
    context = {
        "form": form,
        "report": report,
    }
    return render(request, 'supervisor/assign_form.html', context)


@login_required
@group_required(GroupEnum.supervisor)
def auto_assign_reports(request):
    """
    Automatically assigns service reports to engineers if suitable matches are found.

    TODO: further testing and optimisation where needed
     """

    errors = None
    reports_assigned_count = 0
    try:
        reports = ServiceReport.objects.all().filter(report_status=ServiceReport.ReportStatus.PENDING)
        group = Group.objects.get(name="Engineering")
        engineers = UserModel.objects.all().filter(groups=group)

        for report in reports:
            for engineer in engineers:
                if engineer.appuserprofile.expertise == report.report_type:
                    create_assignment_object(request.user, report, engineer)
                    report_is_assigned(report, engineer)
                    reports_assigned_count += 1
    except Exception as errors:
        pass
    no_errors_message = f"{reports_assigned_count} reports were automatically assigned!"
    context = {"errors": no_errors_message}
    if errors:
        context[errors] = errors
    return render(request, "supervisor/auto_assign_status.html", context)


class ShowAllAssignments(LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """ TODO: search, pagination"""
    group_required = [GroupEnum.supervisor, GroupEnum.engineering, GroupEnum.contractors]
    template_name = 'supervisor/show_all_assignments.html'
    model = Assignment
    ordering = ["-last_updated"]
    filter_set = None

    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = initial_query_set_assignments(self.request, queryset)
        building = self.request.GET.get("building", "")
        report_type = self.request.GET.get("report_type", "")
        if building:
            queryset = queryset.filter(user__appuserprofile__company__additionaladdressinformation__building=building)
        if report_type:
            queryset = queryset.filter(service_report__report_type=report_type)
        self.filter_set = AssignmentFilter(self.request.GET, queryset=queryset)

        return self.filter_set.qs

    def get_paginate_by(self, queryset):
        paginator = self.request.GET.get("paginator", "")
        if paginator:
            self.paginate_by = paginator
        return paginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        buildings = Building.objects.all()
        reports = ServiceReport.objects.all()
        context.update(
            {
                "form": self.filter_set.form,
                "buildings": buildings,
                "building": self.request.GET.get("building", ""),
                "reports": reports,
                "report": self.request.GET.get("report_type", ""),
                "meeting_required": self.request.GET.get("meeting_required", ""),
                "assignment_status": self.request.GET.get("assignment_status", ""),
                "expense_estimate_available": self.request.GET.get("expense_estimate_available", ""),
                "paginator": self.request.GET.get("paginator", ""),
            }
        )

        return context


class ShowAssignmentDetails(LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.supervisor, GroupEnum.engineering, GroupEnum.contractors]
    template_name = 'supervisor/assignment_details.html'
    model = Assignment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user and self.request.user != self.object.assigned_by \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied

        return context


class EditAssignment(LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.supervisor, GroupEnum.contractors]
    template_name = 'supervisor/edit_assignment.html'
    model = Assignment
    fields = ["user"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.assigned_by \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied

        return context

    def form_valid(self, form):
        assignment = form.save(commit=False)
        assignment.assignment_status = Assignment.AssignmentStatus.PENDING
        form.save()
        return super(EditAssignment, self).form_valid(form)


class DeleteAssignment(LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.supervisor]
    template_name = 'supervisor/delete_assignment.html'
    model = Assignment
    success_url = reverse_lazy('show all assignments')
