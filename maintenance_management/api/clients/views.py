from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.clients.serializers import ServiceReportSerializer, ReviewSerializer
from maintenance_management.clients.models import ServiceReport, Review


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_service_reports(request):
    if request.method == "GET":
        reports = ServiceReport.objects.all()
        serializer = ServiceReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        pass  # service report creation


@api_view(["GET", "PATCH", "DELETE"])
@csrf_exempt
def get_service_report_by_id(request, pk):
    if request.method == "GET":
        report = get_object_or_404(ServiceReport, pk=pk)
        if report:
            serializer = ServiceReportSerializer(report)
            return JsonResponse(serializer.data, safe=False)

        return


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PATCH", "DELETE"])
@csrf_exempt
def get_review_by_id(request, pk):
    if request.method == "GET":
        review = get_object_or_404(Review, pk=pk)
        if review:
            serializer = ServiceReportSerializer(review)
            return JsonResponse(serializer.data, safe=False)

        return
