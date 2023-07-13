from django.contrib import admin

from maintenance_management.clients.models import ServiceReport, Review


@admin.register(ServiceReport)
class ServiceReportAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
