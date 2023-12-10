from django.urls import path

from maintenance_management.api.accounts.views import get_all_profiles, get_user_by_id, get_profile_by_id

urlpatterns = [
    path("profiles/", get_all_profiles, name="api_get_all_profiles"),
    path("profiles/<int:pk>/", get_profile_by_id, name="api_get_profile_by_id"),
    path("app-user/<int:pk>/", get_user_by_id, name="api_get_user-by_id"),
]