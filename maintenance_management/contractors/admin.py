from django.contrib import admin

from maintenance_management.contractors.models import ContractorProfile


@admin.register(ContractorProfile)
class ContractorAdmin(admin.ModelAdmin):
    pass
