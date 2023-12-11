from django.contrib.auth import get_user_model
from rest_framework import serializers

from maintenance_management.accounts.models import AppUserProfile, AppUser

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUserProfile
        fields = '__all__'


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            "password": {'write_only': True}
        }
