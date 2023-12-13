import base64
import random

from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.accounts.serializers import ProfileSerializer
from maintenance_management.api.clients.serializers import ReviewSerializer
from maintenance_management.api.common.serializers import CompanySerializer, AddressSerializer
from maintenance_management.api.estate.serializers import BuildingSerializer
from maintenance_management.common.helper_function import get_queries_as_list, verify_constants
from maintenance_management.common.models import Company
from maintenance_management.common.views import TENANTS_DISPLAYED_ON_HOME_PAGE, BUILDINGS_DISPLAYED_ON_HOME_PAGE, \
    REVIEWS_DISPLAYED_ON_HOME_PAGE


@api_view(["GET"])
@csrf_exempt
def show_all_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PATCH"])
@csrf_exempt
def get_company_by_id(request, pk):
    if request.method == "GET":
        company = get_object_or_404(Company, pk=pk)
        if company:
            serializer = CompanySerializer(company)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "PATCH":
        company = get_object_or_404(Company, pk=pk)
        if company:
            data = request.data
            if not data["file"]:
                company.file = None
            else:
                image_as_string = data["file"]
                file_name = data["filename"]
                extension = data["extension"]
                try:
                    image_data = base64.b64decode(image_as_string)
                    company.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
                except Exception as error:
                    print(error)
                    return HttpResponse(status=400)

            company.name = data.get("name", company.name)
            company.business_field = data.get("business_field", company.business_field)
            company.additional_information = data.get("additional_information", company.additional_information)
            company.save()
            return JsonResponse({"call was successful": "asd"})
    return


@api_view(["GET"])
@csrf_exempt
def get_company_address(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if company:
        address = company.additionaladdressinformation_set.first()
        serializer = AddressSerializer(address)

        return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
@csrf_exempt
def get_company_employees(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if company:
        employees = company.appuserprofile_set.all()
        serializer = ProfileSerializer(employees, many=True)

        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@csrf_exempt
def generate_homepage(request):
    tenants, buildings, reviews = get_queries_as_list()

    tenants_count = verify_constants(tenants, TENANTS_DISPLAYED_ON_HOME_PAGE)
    buildings_count = verify_constants(buildings, BUILDINGS_DISPLAYED_ON_HOME_PAGE)
    reviews_count = verify_constants(reviews, REVIEWS_DISPLAYED_ON_HOME_PAGE)

    tenants = random.sample(tenants, k=tenants_count)
    buildings = random.sample(buildings, k=buildings_count)
    reviews = random.sample(reviews, k=reviews_count)
    data = dict()
    data['reviews'] = ReviewSerializer(reviews, many=True).data
    data['tenants'] = CompanySerializer(tenants, many=True).data
    data['buildings'] = BuildingSerializer(buildings, many=True).data
    return JsonResponse(data, safe=False)
