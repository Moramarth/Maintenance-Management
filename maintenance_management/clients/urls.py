from django.urls import path
from .views import show_profile_details

urlpatterns = [
    path("profile/<int:pk>/", show_profile_details, name="profile details")
]