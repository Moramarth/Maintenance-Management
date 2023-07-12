from django.urls import path, include

from .views import ShowAllMeetings, CreateMeeting, ShowMeetingDetails, EditMeeting, DeleteMeeting, \
    ShowAllExpensesEstimates, CreateExpensesEstimate, ShowExpensesEstimateDetails, EditExpensesEstimate, \
    DeleteExpensesEstimate

urlpatterns = [
    path("meetings/",
         include([
             path("", ShowAllMeetings.as_view(), name="show all meetings"),
             path("create/", CreateMeeting.as_view(), name="create meeting"),
             path("<int:pk>/", ShowMeetingDetails.as_view(), name="meeting details"),
             path("<int:pk>/edit/", EditMeeting.as_view(), name="edit meeting"),
             path("<int:pk>/delete/", DeleteMeeting.as_view(), name="delete meeting"),
         ])),

    path("offers/", include([
        path("", ShowAllExpensesEstimates.as_view(), name="show all expenses"),
        path("create/", CreateExpensesEstimate.as_view(), name="create expense"),
        path("<int:pk>/", ShowExpensesEstimateDetails.as_view(), name="expense details"),
        path("<int:pk>/edit/", EditExpensesEstimate.as_view(), name="edit expense"),
        path("<int:pk>/delete/", DeleteExpensesEstimate.as_view(), name="delete expense"),
    ]))

]
