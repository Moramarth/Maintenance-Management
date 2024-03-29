import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from maintenance_management.api.clients.serializers import ServiceReportSerializer, ReviewSerializer

from maintenance_management.api.mixins import UpdateWithImageFieldMixin, UpdateDeleteIfOwnerMixin, DeleteIfOwnerMixin

from maintenance_management.clients.models import ServiceReport, Review
from maintenance_management.common.models import Company

UserModel = get_user_model()


class ServiceReportListCreateView(generics.ListCreateAPIView):
    queryset = ServiceReport.objects.all()
    serializer_class = ServiceReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    image_as_string = None
    file_name = None
    extension = None

    def create(self, request, *args, **kwargs):
        data = request.data
        self.image_as_string = data.get("file", None)
        if self.image_as_string:
            del data["file"]
            self.file_name = data["filename"]
            del data["filename"]
            self.extension = data["extension"]
            del data["extension"]

        company = Company.objects.get(pk=request.user.appuserprofile.company.id)
        data['company'] = company.id
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.image_as_string:
            instance = serializer.save()
            image_data = base64.b64decode(self.image_as_string)
            instance.file.save(name=f"{self.file_name}{self.extension}", content=ContentFile(image_data), save=True)
        else:
            serializer.save()


class ServiceReportDetailsUpdateDeleteView(UpdateWithImageFieldMixin, DeleteIfOwnerMixin,
                                           generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceReport.objects.all()
    serializer_class = ServiceReportSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def can_edit(self):
        return self.request.user == self.get_object().user

    def can_delete(self):
        return self.request.user == self.get_object().user


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReviewDetailsUpdateDelete(UpdateDeleteIfOwnerMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def can_edit(self):
        return self.request.user == self.get_object().user

    def can_delete(self):
        return self.request.user == self.get_object().user
