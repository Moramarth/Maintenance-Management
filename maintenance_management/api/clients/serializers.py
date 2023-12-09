from rest_framework import serializers

from maintenance_management.clients.models import Review, ServiceReport


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ServiceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReport
        fields = '__all__'
