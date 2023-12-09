from rest_framework import serializers

from maintenance_management.accounts.models import AppUserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUserProfile
        fields = '__all__'
