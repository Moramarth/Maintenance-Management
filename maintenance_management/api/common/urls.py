from django.urls import path

from maintenance_management.api.common.views import show_all_companies, generate_homepage, get_company_by_id, \
    get_company_address

urlpatterns = [
    path("companies/", show_all_companies, name="api_show_all_companies"),
    path("companies/<int:pk>/", get_company_by_id, name="api_get_company_by_id"),
    path('companies/<int:pk>/address/', get_company_address, name='api_get_company_address'),
    path("home-page/", generate_homepage, name="api_generate_homepage"),
]
