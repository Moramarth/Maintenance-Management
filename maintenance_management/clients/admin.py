from django.contrib import admin

from maintenance_management.clients.models import ServiceReport


@admin.register(ServiceReport)
class ServiceReportAdmin(admin.ModelAdmin):
    pass
