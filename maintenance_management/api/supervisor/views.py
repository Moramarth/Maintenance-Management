from rest_framework import generics

from maintenance_management.api.supervisor.serializers import AssignmentSerializer
from maintenance_management.supervisor.models import Assignment


class AssignmentDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = "pk"


class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
