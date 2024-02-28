from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from maintenance_management.api.accounts.views import ProfileListView, UserModelDetailsView, ProfileDetailsUpdateView, \
    get_current_user, RegistrationInvitationCreateView

urlpatterns = [
    path("profiles/", ProfileListView.as_view(), name="api_get_all_profiles"),
    path("profiles/<int:pk>/", ProfileDetailsUpdateView.as_view(), name="api_get_profile_by_id"),
    path("app-user/<int:pk>/", UserModelDetailsView.as_view(), name="api_get_user_by_id"),
    path("app-user/current/", get_current_user, name="api_get_current_user"),
    path("register-invite/", RegistrationInvitationCreateView.as_view(), name="api_registration_invitation"),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
