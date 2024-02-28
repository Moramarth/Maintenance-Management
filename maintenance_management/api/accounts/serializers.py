from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from maintenance_management.accounts.models import AppUserProfile, RegisterInvitation
from maintenance_management.common.models import Company

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


class RegistrationInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterInvitation
        fields = "__all__"
        extra_kwargs = {
            "unique_identifier": {"read_only": True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        group = Group.objects.all().filter(name=request.user.groups.name)
        company = Company.objects.all().filter(pk=request.user.appuserprofile.company.pk)
        validated_data['groups'] = group
        validated_data['company'] = company

        instance = super().create(validated_data)

        return instance
