from django.contrib import admin

from maintenance_management.clients.models import ServiceReport, Review


@admin.register(ServiceReport)
class ServiceReportAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "report_type", "report_status", "submit_date"]
    list_display_links = ["title"]
    list_filter = ["report_status", "report_type"]
    ordering = ["submit_date"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "rating", "service_report", "submitted"]
    list_display_links = ["rating"]
    list_filter = ["rating"]
    date_hierarchy = "submitted"
