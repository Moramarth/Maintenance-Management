from django.urls import path
from .views import assign_report_to_engineer_or_contractor, auto_assign_reports

urlpatterns = [
    path("assign-report/<int:pk>/", assign_report_to_engineer_or_contractor, name='assign report'),
    path("auto-assign/", auto_assign_reports, name='auto assign'),
]
