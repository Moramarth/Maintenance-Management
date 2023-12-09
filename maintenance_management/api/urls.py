from django.urls import path

from maintenance_management.api.views import show_all_buildings, show_all_companies, show_all_reviews, \
    show_all_service_reports, generate_homepage, get_all_profiles

urlpatterns = [
    path("buildings/", show_all_buildings, name="api_show_all_buildings"),
    path("companies/", show_all_companies, name="api_show_all_companies"),
    path("reviews/", show_all_reviews, name="api_show_all_reviews"),
    path("service-reports/", show_all_service_reports, name="api_show_all_service_reports"),
    path("home-page/", generate_homepage, name="api_generate_homepage"),
    path("profiles/", get_all_profiles, name="api_get_all_profiles")
]
