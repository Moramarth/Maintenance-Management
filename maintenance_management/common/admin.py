from django.contrib import admin

from maintenance_management.common.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "business_field"]
    search_fields = ["name", "business_field"]
    search_help_text = "Search for a company name or business field"
