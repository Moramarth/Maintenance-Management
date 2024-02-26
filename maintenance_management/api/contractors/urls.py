from django.urls import path

from maintenance_management.api.contractors.views import MeetingListCreateView, MeetingDetailsUpdateDelete, \
    ExpensesEstimateListCreateView, ExpensesEstimateDetailsUpdateDeleteView

urlpatterns = [
    path("meetings/", MeetingListCreateView.as_view(), name="api_show_all_meetings"),
    path("meetings/<int:pk>/", MeetingDetailsUpdateDelete.as_view(), name="api_get_meeting_by_id"),
    path("expenses-estimates/", ExpensesEstimateListCreateView.as_view(), name="api_show_all_expenses_estimates"),
    path("expenses-estimates/<int:pk>/", ExpensesEstimateDetailsUpdateDeleteView.as_view(),
         name="api_get_expenses_estimate_by_id"),
]
