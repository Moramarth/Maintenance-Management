from django.urls import path, include
from .views import register_user_view, AppUserProfileDetails, LogoutUserView, LoginUserView, RegistrationInviteView, \
    EditAppUserProfile
from .signals import *

urlpatterns = [
    path("invite/", RegistrationInviteView.as_view(), name='register invite'),
    path("register/<uuid:unique_identifier>/", register_user_view, name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path("profile/<int:pk>/",
         include([
             path("", AppUserProfileDetails.as_view(), name='profile details'),
             path("edit/", EditAppUserProfile.as_view(), name='edit profile'),
         ])),
]
