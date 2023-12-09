from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.clients.serializers import ServiceReportSerializer, ReviewSerializer
from maintenance_management.clients.models import ServiceReport, Review


@api_view(["GET"])
@csrf_exempt
def show_all_service_reports(request):
    reports = ServiceReport.objects.all()
    serializer = ServiceReportSerializer(reports, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@csrf_exempt
def show_all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)