from rest_framework import serializers

from maintenance_management.accounts.models import AppUserProfile, AppUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUserProfile
        fields = '__all__'


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
