import pathlib

from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.common.models import Company
from maintenance_management.contractors.filters import initial_query_set_meeting_filter, \
    initial_query_set_expenses_estimate_filter, first_and_last_name_filter_for_expenses_estimate_and_meeting
from maintenance_management.contractors.forms import MeetingForm
from maintenance_management.contractors.models import Meeting, ExpensesEstimate
from maintenance_management.supervisor.models import Assignment


class ShowAllMeetings(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """
    Uses 'maintenance_management.common.context_processors.context_forms_and_common_queries' for extra context
    """
    group_required = [GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'contractors/show_all_meetings.html'
    model = Meeting
    ordering = ["meeting_date"]

    _DEFAULT_PAGINATE_BY = 5

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = initial_query_set_meeting_filter(self.request, queryset)
        building = self.request.GET.get("building", "")
        name = self.request.GET.get("name", "")
        if building:
            queryset = queryset.filter(
                assignment__service_report__user__appuserprofile__company__additionaladdressinformation__building=
                building)
        if name:
            queryset = first_and_last_name_filter_for_expenses_estimate_and_meeting(name, queryset)
        return queryset

    def get_paginate_by(self, queryset):
        paginator = self.request.GET.get("paginator", None)
        if not paginator:
            return ShowAllMeetings._DEFAULT_PAGINATE_BY
        return paginator


class CreateMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    success_url = reverse_lazy('show all meetings')
    form_class = MeetingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        context.update({
            "assignment": assignment
        })
        return context

    def form_valid(self, form):
        meeting = form.save(commit=False)
        assignment = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        meeting.assignment = assignment
        meeting.created_by = self.request.user
        form.save()
        return super(CreateMeeting, self).form_valid(form)


class ShowMeetingDetails(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'contractors/meeting_details.html'
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by \
                    and self.request.user != self.object.assignment.assigned_by:
                raise PermissionDenied

        return context


class EditMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    success_url = reverse_lazy('show all meetings')
    form_class = MeetingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by:
                raise PermissionDenied

        return context


class DeleteMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/delete_meeting.html'
    model = Meeting
    success_url = reverse_lazy('show all meetings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by:
                raise PermissionDenied

        return context


class ShowAllExpensesEstimates(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """
    Uses 'maintenance_management.common.context_processors.context_forms_and_common_queries'
    for paginator_form and search_by_name_form
    """
    group_required = [GroupEnum.contractors, GroupEnum.supervisor]
    template_name = 'contractors/show_all_expenses.html'
    model = ExpensesEstimate
    ordering = ["title"]

    _DEFAULT_PAGINATE_BY = 5

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = initial_query_set_expenses_estimate_filter(self.request, queryset)
        company = self.request.GET.get("company", "")
        name = self.request.GET.get("name", "")
        if name:
            queryset = first_and_last_name_filter_for_expenses_estimate_and_meeting(name, queryset)
        if company:
            queryset = queryset.filter(created_by__appuserprofile__company=company)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = Company.objects.all()
        context.update({
            "companies": companies,
        })
        return context

    def get_paginate_by(self, queryset):
        paginator = self.request.GET.get("paginator", None)
        if not paginator:
            return ShowAllExpensesEstimates._DEFAULT_PAGINATE_BY
        return paginator


class CreateExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = ["title", "additional_information", "file"]
    success_url = reverse_lazy('show all expenses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        context.update({
            "assignment": assignment
        })
        return context

    def form_valid(self, form):
        expense_estimate = form.save(commit=False)
        assignment = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        expense_estimate.created_by = self.request.user
        expense_estimate.assignment = assignment
        form.save()
        return super(CreateExpensesEstimate, self).form_valid(form)


class ShowExpensesEstimateDetails(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.contractors, GroupEnum.supervisor]
    template_name = 'contractors/expense_details.html'
    model = ExpensesEstimate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied

        return context


class EditExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = ["title", "additional_information", "file"]
    success_url = reverse_lazy('show all expenses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by:
                raise PermissionDenied

        return context


class DeleteExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/delete_expenses.html'
    model = ExpensesEstimate
    success_url = reverse_lazy('show all expenses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.created_by:
                raise PermissionDenied

        return context


def download_file(request, pk):
    expense = get_object_or_404(ExpensesEstimate, pk=pk)
    extension = pathlib.Path(expense.file.name).suffix
    filename_with_extension = f"Offer-{expense.pk}-{expense.created_by}-{expense.title[:20]}{extension}"
    return FileResponse(expense.file, as_attachment=True, filename=filename_with_extension)
