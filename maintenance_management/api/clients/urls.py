from django.urls import path

from maintenance_management.api.clients.views import show_all_reviews, show_all_service_reports, \
    get_service_report_by_id, get_review_by_id

urlpatterns = [
    path("reviews/", show_all_reviews, name="api_show_all_reviews"),
    path("reviews/<int:pk>/", get_review_by_id, name="api_get_review_by_id"),
    path("service-reports/", show_all_service_reports, name="api_show_all_service_reports"),
    path("service-reports/<int:pk>/", get_service_report_by_id, name="api_get_service_report_by_id"),
]