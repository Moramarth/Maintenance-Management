from django.urls import path, include

urlpatterns = [
    path("", include('maintenance_management.api.common.urls')),
    path("accounts/", include('maintenance_management.api.accounts.urls')),
    path("clients/", include('maintenance_management.api.clients.urls')),
    path("estate/", include('maintenance_management.api.estate.urls')),
]
