from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.accounts.mixins import GroupRequiredMixin
from maintenance_management.clients.filters import initial_query_set_service_report_filter, ServiceReportFilter, \
    first_and_last_name_filter_for_service_report
from maintenance_management.clients.forms import RatingSelectionFilterForm
from maintenance_management.clients.models import ServiceReport, Review
from maintenance_management.common.forms import PaginateByForm, SearchByNameForm
from maintenance_management.estate.models import Building


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
    template_name = 'clients/delete_service_report.html'
    model = ServiceReport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user != self.object.user:
                raise PermissionDenied

        return context


class ShowAllReports(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.ListView):
    """
    Visualises service report information based on Roles

    Filters for the user are available
    """
    group_required = [GroupEnum.clients, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'clients/show_all_service_reports.html'
    model = ServiceReport
    ordering = ["-last_updated"]
    filter_set = None

    _DEFAULT_PAGINATE_BY = 5

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = initial_query_set_service_report_filter(self.request, queryset)
        building = self.request.GET.get("building", "")
        name = self.request.GET.get("name", "")
        if building:
            queryset = queryset.filter(
                company__additionaladdressinformation__building=building
            )
        if name:
            queryset = first_and_last_name_filter_for_service_report(name, queryset)
        self.filter_set = ServiceReportFilter(self.request.GET, queryset)
        return self.filter_set.qs

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginator", ShowAllReports._DEFAULT_PAGINATE_BY)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        buildings = Building.objects.all()
        context.update(
            {
                "paginator_form": PaginateByForm(self.request.GET),
                "service_report_filter_form": self.filter_set.form,
                "search_by_name_form": SearchByNameForm(self.request.GET),
                "buildings": buildings,
            }
        )
        return context


class ShowReportDetails(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.DetailView):
    group_required = [GroupEnum.clients, GroupEnum.contractors, GroupEnum.engineering, GroupEnum.supervisor]
    template_name = 'clients/service_report_details.html'
    model = ServiceReport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            if self.request.user.groups.name == str(GroupEnum.engineering.value) \
                    and (self.object.report_type == ServiceReport.ReportType.OTHER
                         or self.object.report_type == self.request.user.appuserprofile.expertise):
                pass
            elif self.request.user.appuserprofile.company == self.object.user.appuserprofile.company:
                pass
            elif self.request.user != self.object.user \
                    and self.request.user != self.object.assigned_to \
                    and self.request.user.groups.name != str(GroupEnum.supervisor.value):
                raise PermissionDenied

        return context


class ShowAllReviews(views.ListView):
    template_name = 'clients/show_all_reviews.html'
    ordering = ["-submitted"]
    model = Review

    _DEFAULT_PAGINATE_BY = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        rating_filter = self.request.GET.get("rating_filter", "0")
        if rating_filter != "0":
            queryset = queryset.filter(rating=rating_filter)
        return queryset

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginator", ShowAllReviews._DEFAULT_PAGINATE_BY)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "paginator_form": PaginateByForm(self.request.GET),
                "rating_filter_form": RatingSelectionFilterForm(self.request.GET),
            }
        )
        return context


class CreateReview(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.CreateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_review.html'
    model = Review
    fields = ["rating", "comment"]
    success_url = reverse_lazy('show all reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_report = get_object_or_404(ServiceReport, pk=self.kwargs['pk'])
        context.update({
            "service_report": service_report
        })
        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        service_report = get_object_or_404(ServiceReport, pk=self.kwargs['pk'])
        review.user = self.request.user
        review.service_report = service_report
        form.save()
        return super(CreateReview, self).form_valid(form)


class ShowReviewDetails(views.DetailView):
    template_name = 'clients/review_details.html'
    model = Review


class EditReview(auth_mixins.LoginRequiredMixin, GroupRequiredMixin, views.UpdateView):
    group_required = [GroupEnum.clients]
    template_name = 'clients/create_review.html'
    model = Review
    fields = ["rating", "comment"]
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
