from django.contrib import admin

from maintenance_management.supervisor.models import SupervisorProfile


@admin.register(SupervisorProfile)
class SupervisorAdmin(admin.ModelAdmin):
    pass
