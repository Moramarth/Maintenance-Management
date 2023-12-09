from django.urls import path

from maintenance_management.api.clients.views import show_all_reviews, show_all_service_reports

urlpatterns = [
    path("reviews/", show_all_reviews, name="api_show_all_reviews"),
    path("service-reports/", show_all_service_reports, name="api_show_all_service_reports"),
]