from django.contrib import admin

from maintenance_management.estate.models import Building, AdditionalAddressInformation


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "address"]
    list_filter = ["city"]
    exclude = ["latitude", "longitude"]
    view_on_site = True
    change_form_template = 'admin/admin_form_template.html'

    def save_model(self, request, obj, form, change):
        obj.latitude = request.POST.get("latitude")
        obj.longitude = request.POST.get("longitude")
        super().save_model(request, obj, form, change)




@admin.register(AdditionalAddressInformation)
class AdditionalAddressInformationAdmin(admin.ModelAdmin):
    list_display = ["building", "company", "section", "floor", "office_number"]
    list_filter = ["building"]
