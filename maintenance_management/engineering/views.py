from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from maintenance_management.accounts.decorators import group_required
from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.helper_functions import create_assignment_object, report_is_assigned
from maintenance_management.supervisor.models import Assignment

UserModel = get_user_model()


@login_required()
@group_required(GroupEnum.engineering)
def assign_report_to_self(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    create_assignment_object(request.user, report, request.user)
    report_is_assigned(report, request.user)
    return redirect('report details', pk=report.pk)


@login_required
@group_required(GroupEnum.engineering, GroupEnum.contractors)
def accept_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.user != request.user and assignment.user is not None:
        raise PermissionDenied
    assignment.assignment_status = Assignment.AssignmentStatus.ACCEPTED
    assignment.save()
    context = {"assignment": assignment}
    return render(request, "engineering/accept_confirmation.html", context)


@login_required
@group_required(GroupEnum.engineering, GroupEnum.contractors)
def reject_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.user != request.user and assignment.user is not None:
        raise PermissionDenied
    assignment.assignment_status = Assignment.AssignmentStatus.REJECTED
    assignment.user = None
    assignment.save()
    context = {"assignment": assignment}
    return render(request, "engineering/accept_confirmation.html", context)
