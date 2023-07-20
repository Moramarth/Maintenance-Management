from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.contractors.models import Meeting, ExpensesEstimate
from maintenance_management.supervisor.models import Assignment


class ShowAllMeetings(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """ TODO: search, filters, pagination"""
    group_required = [GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'contractors/meetings_list.html'
    model = Meeting

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.request.user.groups.name == str(GroupEnum.supervisor.value):
            return queryset
        return queryset.filter(
            Q(created_by=self.request.user)
            | Q(assignment__assigned_by=self.request.user)
        )


class CreateMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    fields = ["description", "meeting_date"]
    success_url = reverse_lazy('show all meetings')

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
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            if self.request.user != self.object.created_by \
                    and self.request.user != self.object.assignment.assigned_by:
                raise PermissionDenied
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object

        context.update(kwargs)
        return super().get_context_data(**context)


class EditMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    fields = ["description", "meeting_date"]
    success_url = reverse_lazy('show all meetings')


class DeleteMeeting(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/delete_meeting.html'
    model = Meeting
    success_url = reverse_lazy('show all meetings')


class ShowAllExpensesEstimates(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """ TODO: search, filters, pagination """
    group_required = [GroupEnum.contractors, GroupEnum.supervisor]
    template_name = 'contractors/expenses_list.html'
    model = ExpensesEstimate

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.request.user.groups.name == str(GroupEnum.supervisor.value):
            return queryset
        return queryset.filter(created_by=self.request.user)


class CreateExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = ["title", "additional_information", "attached_file"]
    success_url = reverse_lazy('show all expenses')

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
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            if self.request.user != self.object.created_by \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object

        context.update(kwargs)
        return super().get_context_data(**context)


class EditExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = ["title", "additional_information", "attached_file"]
    success_url = reverse_lazy('show all expenses')


class DeleteExpensesEstimate(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.contractors]
    template_name = 'contractors/delete_expenses.html'
    model = ExpensesEstimate
    success_url = reverse_lazy('show all expenses')
