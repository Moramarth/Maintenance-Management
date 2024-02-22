from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.decorators import group_required
from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.filters import AssignmentFilter, initial_query_set_assignments_filter, \
    first_and_last_name_filter_for_assignment
from maintenance_management.supervisor.forms import AssignForm, AssignmentEditByEngineerForm
from maintenance_management.supervisor.helper_functions import create_assignment_object, report_is_assigned, \
    report_auto_assign
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


@login_required
@group_required(GroupEnum.supervisor, GroupEnum.engineering)
def assign_report_to_engineer_or_contractor(request, pk):
    """ Manual assignment of service reports to be handled by engineers or contractors"""
    report = get_object_or_404(ServiceReport, pk=pk)
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        form = AssignForm(request.POST or None)
    else:
        form = AssignmentEditByEngineerForm(request.POST or None)
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

    reports_assigned_count = report_auto_assign(request.user)

    if reports_assigned_count == 1:
        message = f"{reports_assigned_count} report was automatically assigned!"
    else:
        message = f"{reports_assigned_count} reports were automatically assigned!"
    context = {"status_message": message}

    return render(request, "supervisor/auto_assign_status.html", context)


@login_required
@group_required(GroupEnum.supervisor)
def reject_service_report(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    report.report_status = ServiceReport.ReportStatus.REJECTED
    report.save()

    return redirect('report details', report.pk)


@login_required
@group_required(GroupEnum.supervisor)
def assignment_is_done(request, pk):
    """ When assignment status set to done, also sets the service report status to "DONE" """
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.assignment_status = Assignment.AssignmentStatus.DONE
    assignment.save()

    report = assignment.service_report
    report.report_status = ServiceReport.ReportStatus.DONE
    report.save()

    return redirect('assignment details', assignment.pk)


class ShowAllAssignments(LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """
    Visualises assignment information based on Roles

    Uses 'maintenance_management.common.context_processors.context_forms_and_common_queries' for extra context

    Filters for the user are available
    """
    group_required = [GroupEnum.supervisor, GroupEnum.engineering, GroupEnum.contractors]
    template_name = 'supervisor/show_all_assignments.html'
    model = Assignment
    ordering = ["-last_updated"]
    filter_set = None

    _DEFAULT_PAGINATE_BY = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = initial_query_set_assignments_filter(self.request, queryset)
        building = self.request.GET.get("building", "")
        report_type = self.request.GET.get("report_type", "")
        name = self.request.GET.get("name", "")
        if building:
            queryset = queryset.filter(
                user__appuserprofile__company__additionaladdressinformation__building=building
            )
        if report_type:
            queryset = queryset.filter(service_report__report_type=report_type)
        if name:
            queryset = first_and_last_name_filter_for_assignment(name, queryset)
        self.filter_set = AssignmentFilter(self.request.GET, queryset=queryset)

        return self.filter_set.qs

    def get_paginate_by(self, queryset):
        paginator = self.request.GET.get("paginator", None)
        if not paginator:
            return ShowAllAssignments._DEFAULT_PAGINATE_BY
        return paginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reports = ServiceReport.objects.all()
        context.update(
            {
                "extra_filter_fields_form": self.filter_set.form,
                "reports": reports,
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
    group_required = [GroupEnum.supervisor, GroupEnum.engineering]
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

    def get_form_class(self):
        form_class = super().get_form_class()
        if self.request.user.groups.name == str(GroupEnum.engineering.value):
            form_class = AssignmentEditByEngineerForm
        return form_class

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
