from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.clients.models import ServiceReport


# Create your views here.

class CreateServiceReport(views.CreateView):
    """ TODO: autopopulate some of the fields """
    template_name = 'clients/create_service_report.html'
    model = ServiceReport
    fields = "__all__"
    success_url = reverse_lazy('show all reports')


class EditServiceReport(views.UpdateView):
    template_name = 'clients/create_service_report.html'
    model = ServiceReport
    fields = ["title", "description", "image"]
    success_url = reverse_lazy('show all reports')


class DeleteServiceReport(views.DeleteView):
    template_name = 'clients/service_report_delete.html'
    model = ServiceReport
    success_url = reverse_lazy('show all reports')


class ShowAllReports(views.ListView):
    """ TODO: search, filters, pagination, dynamic queries for different roles"""
    template_name = 'clients/service_report_list.html'
    model = ServiceReport


class ShowReportDetails(views.DetailView):
    template_name = 'clients/service_report_details.html'
    model = ServiceReport

# TODO: create views for Review model
