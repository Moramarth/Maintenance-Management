from django.urls import path

from maintenance_management.api.accounts.views import get_all_profiles

urlpatterns = [
    path("profiles/", get_all_profiles, name="api_get_all_profiles")
]