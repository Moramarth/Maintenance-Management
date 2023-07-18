from django.urls import path
from .views import show_my_assignments, accept_assignment, reject_assignment, assign_report_to_self, \
    assign_report_to_contractor

urlpatterns = [
    path("", show_my_assignments, name="show my assignments"),
    path("accept/<int:pk>", accept_assignment, name="accept assignment"),
    path("reject/<int:pk>", reject_assignment, name="reject assignment"),
    path("self-assign/<int:pk>/", assign_report_to_self, name="self assign"),
    path("assign-to-contractor/<int:pk>", assign_report_to_contractor, name="assign to contractor"),

]
