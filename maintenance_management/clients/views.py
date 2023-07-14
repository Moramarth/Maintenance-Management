from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.clients.models import ServiceReport, Review


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


class ShowAllReviews(views.ListView):
    template_name = 'clients/show_all_reviews.html'
    model = Review


class CreateReview(views.CreateView):
    template_name = 'clients/create_review.html'
    model = Review
    success_url = reverse_lazy('show all reviews')


class ShowReviewDetails(views.DetailView):
    template_name = 'clients/review_details.html'
    model = Review


class EditReview(views.UpdateView):
    template_name = 'clients/create_review.html'
    model = Review
    success_url = reverse_lazy('show all reviews')


class DeleteReview(views.DeleteView):
    template_name = 'clients/delete_review.html'
    model = Review
    success_url = reverse_lazy('show all reviews')
