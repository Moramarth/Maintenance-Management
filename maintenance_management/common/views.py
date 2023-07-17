from decouple import config
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from maintenance_management.common.models import Company


# Create your views here.

def home_page(request):
    return render(request, 'common/home.html')


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
