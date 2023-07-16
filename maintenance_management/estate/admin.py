from django.contrib import admin

from maintenance_management.estate.models import Building, AdditionalAddressInformation


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "address"]
    list_filter = ["city"]
    view_on_site = True


@admin.register(AdditionalAddressInformation)
class AdditionalAddressInformationAdmin(admin.ModelAdmin):
    list_display = ["building", "company", "section", "floor", "office_number"]
    list_filter = ["building"]