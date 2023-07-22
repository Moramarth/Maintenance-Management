from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.clients.models import ServiceReport, Review


class CreateServiceReport(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_service_report.html'
    model = ServiceReport
    fields = ["title", "description", "image", "report_type"]
    success_url = reverse_lazy('show all reports')

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.company = self.request.user.appuserprofile.company
        form.save()
        return super(CreateServiceReport, self).form_valid(form)


class EditServiceReport(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_service_report.html'
    model = ServiceReport
    fields = ["title", "description", "image"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context


class DeleteServiceReport(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/service_report_delete.html'
    model = ServiceReport
    success_url = reverse_lazy('show all reports')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context


class ShowAllReports(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """ TODO: search, filters, pagination"""
    group_required = [GroupEnum.clients, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'clients/service_report_list.html'
    model = ServiceReport

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.request.user.groups.name == str(GroupEnum.supervisor.value):
            return queryset
        elif self.request.user.groups.name == str(GroupEnum.engineering.value):
            return queryset.filter(
                Q(assigned_to=self.request.user)
                | Q(report_type=self.request.user.appuserprofile.expertise)
                | Q(report_type=ServiceReport.ReportType.OTHER)
            )
        return queryset.filter(
            Q(user=self.request.user)
            | Q(user__appuserprofile__company=self.request.user.appuserprofile.company)
        )


class ShowReportDetails(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.clients, GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'clients/service_report_details.html'
    model = ServiceReport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user and self.request.user != self.object.assigned_to \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied

        return context


class ShowAllReviews(views.ListView):
    template_name = 'clients/show_all_reviews.html'
    model = Review


class CreateReview(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_review.html'
    model = Review
    fields = ["service_report", "rating", "comment"]
    success_url = reverse_lazy('show all reviews')

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        form.save()
        return super(CreateReview, self).form_valid(form)


class ShowReviewDetails(views.DetailView):
    template_name = 'clients/review_details.html'
    model = Review


class EditReview(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_review.html'
    model = Review
    fields = ["service_report", "rating", "comment"]
    success_url = reverse_lazy('show all reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context


class DeleteReview(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DeleteView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/delete_review.html'
    model = Review
    success_url = reverse_lazy('show all reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context
