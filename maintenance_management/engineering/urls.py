from django.urls import path
from .views import accept_assignment, reject_assignment, assign_report_to_self

urlpatterns = [
    path("accept/<int:pk>/", accept_assignment, name="accept assignment"),
    path("reject/<int:pk>/", reject_assignment, name="reject assignment"),
    path("self-assign/<int:pk>/", assign_report_to_self, name="self assign"),
]
