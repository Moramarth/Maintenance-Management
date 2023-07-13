from django.urls import path, include
from .views import (
    register_user_view, AppUserProfileDetails,
    LogoutUserView, LoginUserView,
    RegistrationInviteView, EditAppUserProfile,
    ChangePassword, ChangePasswordDone,
    PasswordResetDone, PasswordReset,
    PasswordResetConfirm, PasswordResetComplete,
)
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
    path("password/",
         include([
             path("change/<int:pk>/", ChangePassword.as_view(), name='change password'),
             path("change-done/", ChangePasswordDone.as_view(), name='change password successful'),
             path("reset/", PasswordReset.as_view(), name='reset password'),
             path("reset-done/", PasswordResetDone.as_view(), name='reset password successful'),
             path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(),
                  name='password_reset_confirm'),
             path('password-reset-complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
         ]))
]
