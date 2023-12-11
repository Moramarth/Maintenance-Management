from rest_framework import serializers

from maintenance_management.common.models import Company
from maintenance_management.estate.models import AdditionalAddressInformation


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalAddressInformation
        fields = '__all__'
