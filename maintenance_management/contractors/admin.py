from django.contrib import admin

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ["created_by", "assignment", "meeting_date"]
    ordering = ["meeting_date"]


@admin.register(ExpensesEstimate)
class ExpensesEstimateAdmin(admin.ModelAdmin):
    # TODO: download file from link
    list_display = ["created_by", "title", "attached_file"]
