import random

from decouple import config
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic as views

from maintenance_management.common.forms import PaginateByForm, SearchByNameForm
from maintenance_management.common.helper_function import get_queries_as_list, verify_constants
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building

TENANTS_DISPLAYED_ON_HOME_PAGE = 3
BUILDINGS_DISPLAYED_ON_HOME_PAGE = 3
REVIEWS_DISPLAYED_ON_HOME_PAGE = 5


def home_page(request):
    tenants, buildings, reviews = get_queries_as_list()

    tenants_count = verify_constants(tenants, TENANTS_DISPLAYED_ON_HOME_PAGE)
    buildings_count = verify_constants(buildings, BUILDINGS_DISPLAYED_ON_HOME_PAGE)
    reviews_count = verify_constants(reviews, REVIEWS_DISPLAYED_ON_HOME_PAGE)

    tenants = random.sample(tenants, k=tenants_count)
    buildings = random.sample(buildings, k=buildings_count)
    reviews = random.sample(reviews, k=reviews_count)

    context = {
        "tenants": tenants,
        "buildings": buildings,
        "reviews": reviews,
    }
    return render(request, 'common/home.html', context)


def register_info(request):
    return render(request, 'common/registration_info_page.html')


class EditCompanyInfo(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'common/edit_company_info.html'
    model = Company
    fields = "__all__"


def redirect_to_admin(request):
    return HttpResponseRedirect(f"{config('DOMAIN_NAME')}admin/")


class CompanyDetails(views.DetailView):
    template_name = 'common/company_details.html'
    model = Company


class ShowAllCompanies(views.ListView):
    template_name = 'common/show_all_companies.html'
    model = Company
    ordering = ["name"]

    _DEFAULT_PAGINATE_BY = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        building = self.request.GET.get("building", "")
        name = self.request.GET.get("name", "")
        if building:
            queryset = queryset.filter(
                additionaladdressinformation__building=building
            )
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginator", ShowAllCompanies._DEFAULT_PAGINATE_BY)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        buildings = Building.objects.all()
        context.update(
            {
                "paginator_form": PaginateByForm(self.request.GET),
                "search_by_name_form": SearchByNameForm(self.request.GET),
                "buildings": buildings,
            }
        )
        return context
