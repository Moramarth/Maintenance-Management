from django.urls import path

from maintenance_management.api.common.views import show_all_companies, generate_homepage, get_company_by_id

urlpatterns = [
    path("companies/", show_all_companies, name="api_show_all_companies"),
    path("companies/<int:pk>/", get_company_by_id, name="api_get_company_by_id"),
    path("home-page/", generate_homepage, name="api_generate_homepage"),
]
