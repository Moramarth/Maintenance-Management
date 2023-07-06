from django.urls import path
from .views import test_email, registration_view

urlpatterns = [
    path("", test_email),
    path("register/<uuid:unique_identifier>/", registration_view)
]
