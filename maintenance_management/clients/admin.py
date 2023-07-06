from django.contrib import admin

from maintenance_management.clients.models import ClientProfile


@admin.register(ClientProfile)
class ClientAdmin(admin.ModelAdmin):
    pass
