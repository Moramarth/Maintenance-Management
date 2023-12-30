from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.api.accounts.serializers import ProfileSerializer, AppUserSerializer
from maintenance_management.api.mixins import UpdateWithImageFieldMixin

UserModel = get_user_model()


class UserModelDetailsView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class ProfileListView(generics.ListAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetailsUpdateView(UpdateWithImageFieldMixin, generics.RetrieveUpdateAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]

    def can_edit(self):
        return self.request.user == self.get_object().user


@api_view(["GET"])
def get_current_user(request):
    if request.user.is_authenticated:
        user = request.user
        serializer = AppUserSerializer(user)
        return Response(serializer.data)

    return HttpResponse(status=400)
