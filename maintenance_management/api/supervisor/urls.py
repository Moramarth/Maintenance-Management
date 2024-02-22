from django.urls import path, include
from .views import AssignmentListView, AssignmentDetailsUpdateDeleteView, auto_assign_reports, \
    assign_report_to_engineer_or_contractor, reject_service_report

urlpatterns = [
    path("auto-assign/", auto_assign_reports, name='api_auto_assign'),
    path("assign-report/<int:pk>/", assign_report_to_engineer_or_contractor, name='api_assign_report'),
    path("reject-report/<int:pk>/", reject_service_report, name='api_reject_report'),
    path("assignments/", include([
        path("", AssignmentListView.as_view(), name='api_show_all_assignments'),
        path("<int:pk>/", AssignmentDetailsUpdateDeleteView.as_view(), name='api_get_assignment_by_id'),
    ]))
]
