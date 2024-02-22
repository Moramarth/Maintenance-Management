from rest_framework import serializers

from maintenance_management.supervisor.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    service_report_title = serializers.SerializerMethodField(read_only=True)
    assigned_to_full_name = serializers.SerializerMethodField(read_only=True)
    assigned_by_full_name = serializers.SerializerMethodField(read_only=True)
    report_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Assignment
        fields = "__all__"

    def get_service_report_title(self, obj):
        return str(obj.service_report)

    def get_assigned_to_full_name(self, obj):
        return obj.user.appuserprofile.full_name

    def get_assigned_by_full_name(self, obj):
        return obj.assigned_by.appuserprofile.full_name

    def get_report_type(self, obj):
        return obj.service_report.report_type
