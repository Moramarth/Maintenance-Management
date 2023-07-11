from django.contrib import admin

from maintenance_management.contractors.models import Meeting, ExpensesEstimate


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass


@admin.register(ExpensesEstimate)
class ExpensesEstimateAdmin(admin.ModelAdmin):
    pass
