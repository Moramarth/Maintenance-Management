from rest_framework import generics, permissions

from maintenance_management.api.estate.serializers import BuildingSerializer
from maintenance_management.estate.models import Building


class BuildingListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuildingDetailsView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]
