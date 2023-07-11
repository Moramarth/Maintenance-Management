from django.urls import path

from .views import home_page, register_info, EditCompanyInfo

urlpatterns = [
    path("", home_page, name='home page'),
    path("register-info/", register_info, name='register info'),
    path("edit-company-info/<int:pk>/", EditCompanyInfo.as_view(), name='edit company'),
]