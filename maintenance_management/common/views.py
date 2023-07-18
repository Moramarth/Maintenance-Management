import random

from decouple import config
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.common.helper_function import get_queries_as_list, verify_constants
from maintenance_management.common.models import Company

# Create your views here.


TENANTS_DISPLAYED_ON_HOME_PAGE = 3
BUILDINGS_DISPLAYED_ON_HOME_PAGE = 2
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


class EditCompanyInfo(views.UpdateView):
    template_name = 'common/edit_company_info.html'
    model = Company
    fields = "__all__"
    success_url = reverse_lazy('home page')


def redirect_to_admin(request):
    return HttpResponseRedirect(f"{config('DOMAIN_NAME')}admin/")


class CompanyDetails(views.DetailView):
    template_name = 'common/company_details.html'
    model = Company


def show_all_companies(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'common/show_all_companies.html', context)
