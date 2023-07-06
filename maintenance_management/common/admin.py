from django.contrib import admin

from maintenance_management.common.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
