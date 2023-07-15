from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect

from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.forms import AssignForm
from maintenance_management.supervisor.helper_functions import create_assignment_object

UserModel = get_user_model()


# Create your views here.
def assign_report_to_engineer_or_contractor(request, pk):
    """ Manual assignment of service reports to be handled by engineers or contractors"""
    report = get_object_or_404(ServiceReport, pk=pk)
    form = AssignForm(request.POST or None)
    if form.is_valid():
        user = UserModel.objects.get(pk=form.cleaned_data["assign_to"])
        create_assignment_object(request.user, report, user)
        report.report_status = ServiceReport.ReportStatus.ASSIGNED
        report.assigned_to = user
        report.save()
        return redirect('report details', pk=report.pk)
    context = {
        "form": form,
        "report": report,
    }
    return render(request, 'supervisor/assign_form.html', context)


def auto_assign_reports(request):
    """
    Automatically assigns service reports to engineers if suitable matches are found.

    TODO: further testing and optimisation where needed
     """

    errors = None
    reports_assigned_count = 0
    try:
        reports = ServiceReport.objects.all().filter(report_status=ServiceReport.ReportStatus.PENDING)
        group = Group.objects.get(name="Engineering")
        engineers = UserModel.objects.all().filter(groups=group)

        for report in reports:
            for engineer in engineers:
                if engineer.appuserprofile.expertise == report.report_type:
                    create_assignment_object(request.user, report, engineer)
                    report.assigned_to = engineer
                    report.report_status = ServiceReport.ReportStatus.ASSIGNED
                    reports_assigned_count += 1
    except Exception as errors:
        pass
    no_errors_message = f"{reports_assigned_count} reports were automatically assigned!"
    context = {"errors": no_errors_message}
    if errors:
        context[errors] = errors
    return render(request, "supervisor/auto_assign_status.html", context)
