from django.urls import path

from maintenance_management.api.clients.views import ReviewListCreateView, ServiceReportListCreateView, \
    ServiceReportDetailsUpdateDeleteView, ReviewDetailsUpdateDelete

urlpatterns = [
    path("reviews/", ReviewListCreateView.as_view(), name="api_show_all_reviews"),
    path("reviews/<int:pk>/", ReviewDetailsUpdateDelete.as_view(), name="api_get_review_by_id"),
    path("service-reports/", ServiceReportListCreateView.as_view(), name="api_show_all_service_reports"),
    path("service-reports/<int:pk>/", ServiceReportDetailsUpdateDeleteView.as_view(),
         name="api_get_service_report_by_id"),
]
