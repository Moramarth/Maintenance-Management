from django.urls import path

from maintenance_management.api.common.views import show_all_companies, generate_homepage

urlpatterns = [
    path("companies/", show_all_companies, name="api_show_all_companies"),
    path("home-page/", generate_homepage, name="api_generate_homepage"),
]
