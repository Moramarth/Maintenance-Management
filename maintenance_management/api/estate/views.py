from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.estate.serializers import BuildingSerializer
from maintenance_management.estate.models import Building


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_buildings(request):
    buildings = Building.objects.all()
    serializer = BuildingSerializer(buildings, many=True)
    return JsonResponse(serializer.data, safe=False)