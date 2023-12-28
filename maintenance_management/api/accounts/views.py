from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import generics
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


class ProfileListView(generics.ListAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailsUpdateView(UpdateWithImageFieldMixin, generics.RetrieveUpdateAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"


@api_view(["GET"])
def get_current_user(request):
    if request.user.is_authenticated:
        user = request.user
        serializer = AppUserSerializer(user)
        return Response(serializer.data)

    return HttpResponse(status=400)

# @api_view(["GET", "PATCH"])
# @csrf_exempt
# def get_profile_by_id(request, pk):
#     if request.method == "GET":
#         profile = get_object_or_404(AppUserProfile, pk=pk)
#         if profile:
#             serializer = ProfileSerializer(profile)
#             return JsonResponse(serializer.data, safe=False)
#     elif request.method == "PATCH":
#         profile = get_object_or_404(AppUserProfile, pk=pk)
#         if profile:
#             data = request.data
#             print(data)
#             if data["file"] is None:
#                 profile.file = None
#             else:
#                 image_as_string = data["file"]
#                 file_name = data["filename"]
#                 extension = data["extension"]
#                 try:
#                     image_data = base64.b64decode(image_as_string)
#                     profile.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
#                 except Exception as error:
#                     print(error)
#                     return HttpResponse(status=400)
#
#             profile.first_name = data.get("first_name", profile.first_name)
#             profile.last_name = data.get("last_name", profile.last_name)
#             profile.phone_number = data.get("phone_number", profile.phone_number)
#             profile.save()
#             return JsonResponse({"call was successful": "asd"})
