from django.urls import path

from .views import home_page, register_info, EditCompanyInfo, redirect_to_admin, CompanyDetails, ShowAllCompanies

urlpatterns = [
    path("", home_page, name='home page'),
    path("to_admin/", redirect_to_admin, name='admin page'),
    path("register-info/", register_info, name='register info'),
    path("partners/", ShowAllCompanies.as_view(), name='show all companies'),
    path("company-details/<int:pk>/", CompanyDetails.as_view(), name='company details'),
    path("edit-company-info/<int:pk>/", EditCompanyInfo.as_view(), name='edit company'),
]
