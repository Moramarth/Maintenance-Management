from rest_framework import generics

from maintenance_management.api.estate.serializers import BuildingSerializer
from maintenance_management.estate.models import Building


class BuildingListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDetailsView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = "pk"
