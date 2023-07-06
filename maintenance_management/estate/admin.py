from django.contrib import admin

from maintenance_management.estate.models import Building, AdditionalAddressInformation


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(AdditionalAddressInformation)
class AdditionalAddressInformationAdmin(admin.ModelAdmin):
    pass
