from rest_framework import serializers

from maintenance_management.clients.models import Review, ServiceReport


class UserAndCompanyFullNameSerializerMixin:
    user_full_name = serializers.SerializerMethodField(read_only=True)
    user_company_name = serializers.SerializerMethodField(read_only=True)

    def get_user_full_name(self, obj):
        if obj.user:
            return obj.user.appuserprofile.full_name
        return None

    def get_user_company_name(self, obj):
        if obj.user:
            return obj.user.appuserprofile.company.name
        return None


class ReviewSerializer(UserAndCompanyFullNameSerializerMixin, serializers.ModelSerializer):
    service_report_title = serializers.SerializerMethodField(read_only=True)
    company_logo = serializers.SerializerMethodField(read_only=True)
    user_profile_picture = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def get_service_report_title(self, obj):
        if obj.service_report:
            return obj.service_report.title
        return None

    def get_company_logo(self, obj):
        if obj.user:
            if obj.user.appuserprofile.company.file:
                return obj.user.appuserprofile.company.file.url
        return None

    def get_user_profile_picture(self, obj):
        if obj.user:
            return obj.user.appuserprofile.file.url or None


class ServiceReportSerializer(UserAndCompanyFullNameSerializerMixin, serializers.ModelSerializer):
    assigned_to_full_name = serializers.SerializerMethodField(read_only=True)
    assigned_to_company_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ServiceReport
        fields = '__all__'

    def get_assigned_to_full_name(self, obj):
        if obj.assigned_to:
            return obj.assigned_to.appuserprofile.full_name
        return None

    def get_assigned_to_company_name(self, obj):
        if obj.assigned_to:
            return obj.assigned_to.appuserprofile.company.name
        return None
