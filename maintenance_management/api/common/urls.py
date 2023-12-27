from django.urls import path

from maintenance_management.api.common.views import CompanyListView, CompanyDetailsUpdateView, \
    get_company_address, get_company_employees

urlpatterns = [
    path("companies/", CompanyListView.as_view(), name="api_show_all_companies"),
    path("companies/<int:pk>/", CompanyDetailsUpdateView.as_view(), name="api_get_company_by_id"),
    path('companies/<int:pk>/address/', get_company_address, name='api_get_company_address'),
    path('companies/<int:pk>/employees/', get_company_employees, name='api_get_company_employees'),
]
