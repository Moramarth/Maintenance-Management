from django.urls import path

from maintenance_management.api.estate.views import show_all_buildings

urlpatterns = [
    path("buildings/", show_all_buildings, name="api_show_all_buildings"),
]