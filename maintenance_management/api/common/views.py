import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from maintenance_management.api.clients.serializers import ReviewSerializer
from maintenance_management.api.common.serializers import CompanySerializer
from maintenance_management.api.estate.serializers import BuildingSerializer
from maintenance_management.common.helper_function import get_queries_as_list, verify_constants
from maintenance_management.common.models import Company
from maintenance_management.common.views import TENANTS_DISPLAYED_ON_HOME_PAGE, BUILDINGS_DISPLAYED_ON_HOME_PAGE, \
    REVIEWS_DISPLAYED_ON_HOME_PAGE


@api_view(["GET", "POST"])
@csrf_exempt
def show_all_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "POST"])
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
