from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


# Create your views here.
class ShowAllMeetings(views.ListView):
    """ TODO: search, filters, pagination, dynamic queries for different roles"""
    template_name = 'contractors/meetings_list.html'
    model = Meeting


class CreateMeeting(views.CreateView):
    """ TODO: autopopulate some of the fields """
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('show all meetings')


class ShowMeetingDetails(views.DetailView):
    template_name = 'contractors/meeting_details.html'
    model = Meeting


class EditMeeting(views.UpdateView):
    template_name = 'contractors/create_meeting.html'
    model = Meeting
    fields = ["description", "meeting_date"]
    success_url = reverse_lazy('show all meetings')


class DeleteMeeting(views.DeleteView):
    template_name = 'contractors/delete_meeting.html'
    model = Meeting
    success_url = reverse_lazy('show all meetings')


class ShowAllExpensesEstimates(views.ListView):
    """ TODO: search, filters, pagination, dynamic queries for different roles"""
    template_name = 'contractors/expenses_list.html'
    model = ExpensesEstimate


class CreateExpensesEstimate(views.CreateView):
    """ TODO: autopopulate some of the fields """
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = '__all__'
    success_url = reverse_lazy('show all expenses')


class ShowExpensesEstimateDetails(views.DetailView):
    template_name = 'contractors/expense_details.html'
    model = ExpensesEstimate


class EditExpensesEstimate(views.UpdateView):
    template_name = 'contractors/create_expenses.html'
    model = ExpensesEstimate
    fields = ["title", "additional_information", "attached_file"]
    success_url = reverse_lazy('show all expenses')


class DeleteExpensesEstimate(views.DeleteView):
    template_name = 'contractors/delete_expenses.html'
    model = ExpensesEstimate
    success_url = reverse_lazy('show all expenses')
