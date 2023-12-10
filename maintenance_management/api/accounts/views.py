from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.accounts.models import AppUserProfile, AppUser
from maintenance_management.api.accounts.serializers import ProfileSerializer, AppUserSerializer


@api_view(["GET"])
@csrf_exempt
def get_all_profiles(request):
    profiles = AppUserProfile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PATCH", "DELETE"])
@csrf_exempt
def get_profile_by_id(request, pk):
    profile = get_object_or_404(AppUser, pk=pk)
    if profile:
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data, safe=False)
    return


@api_view(["GET"])
@csrf_exempt
def get_user_by_id(request, pk):
    user = get_object_or_404(AppUser, pk=pk)
    if user:
        serializer = AppUserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    return
