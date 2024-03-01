from rest_framework import serializers

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


class CreatedByFullNameAndAssignmentAsStringMixin(serializers.Serializer):
    created_by_full_name = serializers.SerializerMethodField(read_only=True)
    assignment_as_string = serializers.SerializerMethodField(read_only=True)

    def get_created_by_full_name(self, obj):
        return obj.created_by.appuserprofile.full_name

    def get_assignment_as_string(self, obj):
        return str(obj.assignment)


class MeetingSerializer(CreatedByFullNameAndAssignmentAsStringMixin, serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class ExpensesEstimateSerializer(CreatedByFullNameAndAssignmentAsStringMixin, serializers.ModelSerializer):
    class Meta:
        model = ExpensesEstimate
        fields = '__all__'
