from django.urls import path, include
from .views import assign_report_to_engineer_or_contractor, auto_assign_reports, ShowAllAssignments, \
    ShowAssignmentDetails, EditAssignment, DeleteAssignment, assignment_is_done, reject_service_report

from .signals import *

urlpatterns = [
    path("assign-report/<int:pk>/", assign_report_to_engineer_or_contractor, name='assign report'),
    path("auto-assign/", auto_assign_reports, name='auto assign'),
    path("reject-report/<int:pk>/", reject_service_report, name='reject report'),
    path("assignments/", include([
        path("", ShowAllAssignments.as_view(), name='show all assignments'),
        path("<int:pk>/", ShowAssignmentDetails.as_view(), name='assignment details'),
        path("<int:pk>/edit/", EditAssignment.as_view(), name='edit assignment'),
        path("<int:pk>/delete/", DeleteAssignment.as_view(), name='delete assignment'),
        path("<int:pk>/done/", assignment_is_done, name='assignment is done'),
    ])),
]
