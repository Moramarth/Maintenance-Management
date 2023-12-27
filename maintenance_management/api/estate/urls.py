from django.urls import path

from maintenance_management.api.estate.views import BuildingListView, BuildingDetailsView

urlpatterns = [
    path("buildings/", BuildingListView.as_view(), name="api_show_all_buildings"),
    path("buildings/<int:pk>/", BuildingDetailsView.as_view(), name="api_get_building_by_id"),
]