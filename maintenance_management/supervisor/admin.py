from django.contrib import admin

from maintenance_management.supervisor.models import Assignment


@admin.register(Assignment)
class AssignmentsAdmin(admin.ModelAdmin):
    list_display = [
        "service_report",
        "user",
        "meeting_required",
        "expense_estimate_available",
        "last_updated",
        "assignment_status",
    ]
    view_on_site = True
    list_filter = ["assignment_status"]
