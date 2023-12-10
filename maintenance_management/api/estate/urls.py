from django.urls import path

from maintenance_management.api.estate.views import show_all_buildings, get_building_by_id

urlpatterns = [
    path("buildings/", show_all_buildings, name="api_show_all_buildings"),
    path("buildings/<int:pk>/", get_building_by_id, name="api_get_building_by_id"),
]