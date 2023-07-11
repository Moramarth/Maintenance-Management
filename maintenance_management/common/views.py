from django.shortcuts import render
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
