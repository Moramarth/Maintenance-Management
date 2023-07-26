from django.contrib import admin

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ["meeting_date", "created_by", "name", "assignment"]
    ordering = ["meeting_date"]

    def name(self, obj):
        return obj.created_by.appuserprofile.full_name


@admin.register(ExpensesEstimate)
class ExpensesEstimateAdmin(admin.ModelAdmin):
    # TODO: download file from link
    list_display = ["title", "created_by", "name", "attached_file"]

    def name(self, obj):
        return obj.created_by.appuserprofile.full_name
