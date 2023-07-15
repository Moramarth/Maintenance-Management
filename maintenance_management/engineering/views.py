from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from maintenance_management.clients.models import ServiceReport
from maintenance_management.engineering.forms import AssignToContractorForm
from maintenance_management.supervisor.helper_functions import create_assignment_object, report_is_assigned
from maintenance_management.supervisor.models import Assignment

# Create your views here.


# TODO: self assign, assign to contractor, accept/reject assignment

UserModel = get_user_model()


def assign_report_to_self(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    create_assignment_object(request.user, report, request.user)
    return redirect('report details', pk=report.pk)


def assign_report_to_contractor(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    form = AssignToContractorForm(request.POST or None)
    if form.is_valid():
        user = UserModel.objects.get(pk=form.cleaned_data["assign_to"])
        create_assignment_object(request.user, report, user)
        report_is_assigned(report, user)

        return redirect('report details', pk=report.pk)


def show_my_assignments(request):
    assignments = Assignment.objects.all().filter(user=request.user)
    context = {
        "assignments": assignments
    }
    return render(request, 'engineering/show_my_assignments.html', context)


def accept_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.assignment_status = Assignment.AssignmentStatus.ACCEPTED
    context = {"assignment": assignment}
    return render(request, "engineering/accept_confirmation.html", context)


def reject_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.assignment_status = Assignment.AssignmentStatus.REJECTED
    assignment.user = None
    context = {"assignment": assignment}
    return render(request, "engineering/accept_confirmation.html", context)
