import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import generics, status
from rest_framework.response import Response

from maintenance_management.api.clients.serializers import ServiceReportSerializer, ReviewSerializer

from maintenance_management.api.mixins import UpdateWithImageFieldMixin

from maintenance_management.clients.models import ServiceReport, Review
from maintenance_management.common.models import Company

UserModel = get_user_model()


class ServiceReportListCreateView(generics.ListCreateAPIView):
    queryset = ServiceReport.objects.all()
    serializer_class = ServiceReportSerializer

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


# @api_view(["GET", "POST"])
# @csrf_exempt
# def show_all_service_reports(request):
#     elif request.method == "POST":
#
#         user, status_code = validate_token(request.data)
#         if user is not None:
#             data = request.data
#             del data["token"]
#             image_as_string = data.get("file", None)
#             if image_as_string:
#                 del data["file"]
#                 file_name = data["filename"]
#                 del data["filename"]
#                 extension = data["extension"]
#                 del data["extension"]
#             company = Company.objects.get(pk=user.appuserprofile.company.id)
#             data['company'] = company.id
#             serializer = ServiceReportSerializer(data=data)
#             if serializer.is_valid():
#                 instance = serializer.save()
#                 if image_as_string:
#                     image_data = base64.b64decode(image_as_string)
#                     instance.file.save(name=f"{file_name}{extension}", content=ContentFile(image_data), save=True)
#
#             return JsonResponse({"call was successful": "asd"})
#
#         response = HttpResponse()
#         response.status_code = status_code
#         return response


class ServiceReportDetailsUpdateDeleteView(UpdateWithImageFieldMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceReport.objects.all()
    serializer_class = ServiceReportSerializer
    lookup_field = 'pk'


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReviewDetailsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
