from django.contrib import admin

from maintenance_management.supervisor.models import Assignments


@admin.register(Assignments)
class AssignmentsAdmin(admin.ModelAdmin):
    pass
