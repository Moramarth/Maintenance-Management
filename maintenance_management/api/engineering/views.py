from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.helper_functions import create_assignment_object, report_is_assigned
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


@api_view(["POST"])
def assign_report_to_self(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    create_assignment_object(request.user, report, request.user)
    report_is_assigned(report, request.user)
    return HttpResponse(status=200)


@api_view(["POST"])
def accept_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.user != request.user and assignment.user is not None:
        return HttpResponse(status=403)
    assignment.assignment_status = Assignment.AssignmentStatus.ACCEPTED
    assignment.save()
    return HttpResponse(status=200)


@api_view(["POST"])
def reject_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.user != request.user and assignment.user is not None:
        return HttpResponse(status=403)
    assignment.assignment_status = Assignment.AssignmentStatus.REJECTED
    assignment.user = None
    assignment.save()
    return HttpResponse(status=200)
