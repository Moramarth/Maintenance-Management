from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from maintenance_management.api.supervisor.serializers import AssignmentSerializer
from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.helper_functions import report_auto_assign, create_assignment_object, \
    report_is_assigned
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


class AssignmentDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = "pk"


class AssignmentListView(generics.ListAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return Assignment.objects.all().order_by("-last_updated")


@api_view(["POST"])
def auto_assign_reports(request):
    """
    Automatically assigns service reports to engineers if suitable matches are found.
    """

    reports_assigned_count = report_auto_assign(request.user)

    return Response({
        "reports_assigned_count": reports_assigned_count
    })


@api_view(["POST"])
def assign_report_to_engineer_or_contractor(request, pk):
    user = UserModel.objects.get(pk=request.data.assigned_to)
    report = get_object_or_404(ServiceReport, pk=pk)
    create_assignment_object(request.user, report, user)
    report_is_assigned(report, user)
    return HttpResponse(status=200)


@api_view(["POST"])
def reject_service_report(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    report.report_status = ServiceReport.ReportStatus.REJECTED
    report.save()
    return HttpResponse(status=200)
