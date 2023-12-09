from rest_framework import serializers

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.clients.models import Review, ServiceReport
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ServiceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReport
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model= AppUserProfile
        fields = '__all__'
