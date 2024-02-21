from django.urls import path, include
from .views import AssignmentListView, AssignmentDetailsUpdateDeleteView

urlpatterns = [
    path("assignments/", include([
        path("", AssignmentListView.as_view(), name='api_show_all_assignments'),
        path("<int:pk>/", AssignmentDetailsUpdateDeleteView.as_view(), name='api_get_assignment_by_id'),
    ]))
]
