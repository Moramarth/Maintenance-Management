from django.urls import path

from .views import ShowAllBuildings, ShowBuildingDetails

urlpatterns = [
    path("", ShowAllBuildings.as_view(), name="show all buildings"),
    path("details/<int:pk>", ShowBuildingDetails.as_view(), name="building details"),
]
