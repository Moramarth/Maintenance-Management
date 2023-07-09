from django.urls import path
from .views import registration_invite_view, register_user_view
from .signals import *

urlpatterns = [
    path("", registration_invite_view, name='register invite'),
    path("register/<uuid:unique_identifier>/", register_user_view, name='register user'),
]
