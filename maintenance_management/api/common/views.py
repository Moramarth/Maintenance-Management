from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response


from maintenance_management.api.accounts.serializers import ProfileSerializer
from maintenance_management.api.common.serializers import CompanySerializer, AddressSerializer
from maintenance_management.api.mixins import UpdateWithImageFieldMixin
from maintenance_management.common.models import Company


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyDetailsUpdateView(UpdateWithImageFieldMixin, generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def can_edit(self):
        return self.request.user.appuserprofile.company_id == self.get_object().id


@api_view(["GET"])
def get_company_address(request, pk):
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    company = get_object_or_404(Company, pk=pk)
    if company:
        address = company.additionaladdressinformation_set.first()
        serializer = AddressSerializer(address)

        return Response(serializer.data)


@api_view(["GET"])
def get_company_employees(request, pk):
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    company = get_object_or_404(Company, pk=pk)
    if company:
        employees = company.appuserprofile_set.all()
        serializer = ProfileSerializer(employees, many=True)

        return Response(serializer.data)
