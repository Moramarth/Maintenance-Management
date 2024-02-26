from rest_framework import generics

from maintenance_management.api.contractors.serializers import MeetingSerializer, ExpensesEstimateSerializer
from maintenance_management.contractors.models import Meeting, ExpensesEstimate


class MeetingListCreateView(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingDetailsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    lookup_field = 'pk'


class ExpensesEstimateListCreateView(generics.ListCreateAPIView):
    queryset = ExpensesEstimate.objects.all()
    serializer_class = ExpensesEstimateSerializer


class ExpensesEstimateDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpensesEstimate.objects.all()
    serializer_class = ExpensesEstimateSerializer
    lookup_field = 'pk'
