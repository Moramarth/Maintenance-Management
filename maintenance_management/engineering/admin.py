from django.contrib import admin

from maintenance_management.engineering.models import EngineeringProfile


@admin.register(EngineeringProfile)
class EngineeringAdmin(admin.ModelAdmin):
    pass
