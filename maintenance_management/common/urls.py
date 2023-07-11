from django.urls import path

from .views import home_page, register_info, EditCompanyInfo, redirect_to_admin

urlpatterns = [
    path("", home_page, name='home page'),
    path("to_admin/", redirect_to_admin, name='admin page'),
    path("register-info/", register_info, name='register info'),
    path("edit-company-info/<int:pk>/", EditCompanyInfo.as_view(), name='edit company'),
]
