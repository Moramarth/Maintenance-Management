from django.urls import path, include
from .views import ShowAllReports, ShowReportDetails, EditServiceReport, DeleteServiceReport, CreateServiceReport, \
    ShowAllReviews, CreateReview, ShowReviewDetails, EditReview, DeleteReview

urlpatterns = [
    path("service-reports/",
         include([
             path("", ShowAllReports.as_view(), name='show all reports'),
             path("create/", CreateServiceReport.as_view(), name='create report'),
             path("<int:pk>/", ShowReportDetails.as_view(), name='report details'),
             path("<int:pk>/edit", EditServiceReport.as_view(), name='edit report'),
             path("<int:pk>/delete", DeleteServiceReport.as_view(), name='delete report'),
         ])),
    # TODO: slug instead of PK?
    path("reviews/",
         include([
             path("", ShowAllReviews.as_view(), name='show all reviews'),
             path("create/", CreateReview.as_view(), name='create review'),
             path("<int:pk>/", ShowReviewDetails.as_view(), name='review details'),
             path("<int:pk>/edit/", EditReview.as_view(), name='edit review'),
             path("<int:pk>/delete/", DeleteReview.as_view(), name='delete review'),
         ])),
]
