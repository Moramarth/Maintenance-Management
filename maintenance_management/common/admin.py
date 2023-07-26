from django.contrib import admin

from maintenance_management.common.models import Company
from maintenance_management.estate.models import AdditionalAddressInformation


class AdditionalAddressInformationInLine(admin.TabularInline):
    model = AdditionalAddressInformation
    extra = 0
    verbose_name_plural = "Company Address"
    verbose_name = "Company Address"


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "business_field"]
    search_fields = ["name", "business_field"]
    search_help_text = "Search for a company name or business field"
    inlines = [AdditionalAddressInformationInLine]
    view_on_site = True
