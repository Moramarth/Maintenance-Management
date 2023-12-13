import base64

import jwt

from decouple import config
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.clients.serializers import ServiceReportSerializer, ReviewSerializer

from maintenance_management.api.helper_functions.token_validation import validate_token

from maintenance_management.clients.models import ServiceReport, Review
from maintenance_management.common.models import Company

UserModel = get_user_model()


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_service_reports(request):
    if request.method == "GET":
        reports = ServiceReport.objects.all()
        serializer = ServiceReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":

        user, status_code = validate_token(request.data)
        if user is not None:
            data = request.data
            del data["token"]
            image_as_string = data.get("file", None)
            if image_as_string:
                del data["file"]
                file_name = data["filename"]
                del data["filename"]
                extension = data["extension"]
                del data["extension"]
            company = Company.objects.get(pk=user.appuserprofile.company.id)
            data['company'] = company.id
            serializer = ServiceReportSerializer(data=data)
            if serializer.is_valid():
                instance = serializer.save()
                if image_as_string:
                    image_data = base64.b64decode(image_as_string)
                    instance.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)


            return JsonResponse({"call was successful": "asd"})

        response = HttpResponse()
        response.status_code = status_code
        return response


@api_view(["GET", "PATCH", "DELETE"])
@csrf_exempt
def get_service_report_by_id(request, pk):
    if request.method == "GET":
        report = get_object_or_404(ServiceReport, pk=pk)
        if report:
            serializer = ServiceReportSerializer(report)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "DELETE":
        report = get_object_or_404(Review, pk=pk)
        if report:
            report.delete()
            return JsonResponse({"call was successful": "asd"})
    elif request.method == "PATCH":
        report = get_object_or_404(ServiceReport, pk=pk)

        if report:
            data = request.data
            if not data["file"]:
                report.file = None
            else:
                image_as_string = data["file"]
                file_name = data["filename"]
                extension = data["extension"]
                try:
                    image_data = base64.b64decode(image_as_string)
                    report.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
                except Exception as error:
                    print(error)
                    return HttpResponse(status=400)

            report.title = data.get("title", report.title)
            report.description = data.get("description", report.description)
            report.save()
            return JsonResponse({"call was successful": "asd"})

        return


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_reviews(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":

        response = HttpResponse()
        try:
            token = request.data["token"]
            del request.data["token"]
            info = jwt.decode(jwt=token, key=config("JWT_SECRET"), algorithms=["HS256"])
            user = UserModel.objects.get(pk=info["id"])
            if not user:
                response.status_code = 400
                return response
        except Exception as e:
            response.status_code = 403
            return response

        data = request.data
        review = {}
        for (key, value) in data.items():
            review[key] = value
        serializer = ReviewSerializer(data=review)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({"call was successful": "asd"})


@api_view(["GET", "PATCH", "DELETE"])
@csrf_exempt
def get_review_by_id(request, pk):
    if request.method == "GET":
        review = get_object_or_404(Review, pk=pk)
        if review:
            serializer = ReviewSerializer(review)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "DELETE":
        review = get_object_or_404(Review, pk=pk)
        if review:
            review.delete()
            return JsonResponse({"call was successful": "asd"})
    elif request.method == "PATCH":
        review = get_object_or_404(Review, pk=pk)

        if review:
            data = request.data

            review.rating = data.get("rating", review.rating)
            review.comment = data.get("comment", review.comment)
            review.save()
            return JsonResponse({"call was successful": "asd"})

        return
