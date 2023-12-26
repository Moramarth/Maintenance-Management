import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.api.accounts.serializers import ProfileSerializer, AppUserSerializer

UserModel = get_user_model()


class UserModelDetailsView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'pk'


class ProfileListView(generics.ListAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = AppUserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if self.request.user != instance.user:
            return HttpResponse(status=403)
        if request.data['file'] is not None:
            image_as_string = request.data.pop("file")
            file_name = request.data.pop("filename")
            extension = request.data.pop("extension")
            try:
                image_data = base64.b64decode(image_as_string)
                instance.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
            except Exception:
                return HttpResponse(status=400)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


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
