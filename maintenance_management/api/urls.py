from django.urls import path, include

urlpatterns = [
    path("", include('maintenance_management.api.common.urls')),
    path("accounts/", include('maintenance_management.api.accounts.urls')),
    path("clients/", include('maintenance_management.api.clients.urls')),
    path("contractors/", include('maintenance_management.api.contractors.urls')),
    path("estate/", include('maintenance_management.api.estate.urls')),
    path("engineering/", include('maintenance_management.api.engineering.urls')),
    path("supervisor/", include('maintenance_management.api.supervisor.urls')),
]
