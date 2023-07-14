from django.contrib import admin

from maintenance_management.supervisor.models import Assignment


@admin.register(Assignment)
class AssignmentsAdmin(admin.ModelAdmin):
    pass
