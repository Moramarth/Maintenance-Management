from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.accounts.models import AppUserProfile
from maintenance_management.api.accounts.serializers import ProfileSerializer


@api_view(["GET", "POST"])
@csrf_exempt
def get_all_profiles(request):
    profiles = AppUserProfile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)