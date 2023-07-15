from django.urls import path, include
from .views import assign_report_to_engineer_or_contractor, auto_assign_reports, ShowAllAssignments, \
    ShowAssignmentDetails, EditAssignment, DeleteAssignment

urlpatterns = [
    path("assign-report/<int:pk>/", assign_report_to_engineer_or_contractor, name='assign report'),
    path("auto-assign/", auto_assign_reports, name='auto assign'),
    path("assignments/", include([
        path("", ShowAllAssignments.as_view(), name='show all assignments'),
        path("<int:pk>/", ShowAssignmentDetails.as_view(), name='assignment details'),
        # TODO: decide to remove, change or leave as it is
        path("<int:pk>/edit/", EditAssignment.as_view(), name='edit assignment'),
        path("<int:pk>/delete/", DeleteAssignment.as_view(), name='delete assignment'),
    ])),
]
