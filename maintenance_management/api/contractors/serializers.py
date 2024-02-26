from rest_framework import serializers

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class ExpensesEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesEstimate
        fields = '__all__'
