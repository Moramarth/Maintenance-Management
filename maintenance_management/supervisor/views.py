from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.forms import AssignForm

UserModel = get_user_model()


# Create your views here.
def assign_report_to_engineer_or_contractor(request, pk):
    report = get_object_or_404(ServiceReport, pk=pk)
    form = AssignForm(request.POST or None)
    if form.is_valid():
        user = UserModel.objects.get(pk=form.cleaned_data["assign_to"])
        report.report_status = "Assigned"
        report.assigned_to = user
        report.save()
        return redirect('report details', pk=report.pk)
    context = {
        "form": form,
        "report": report,
    }
    return render(request, 'supervisor/assign_form.html', context)


def auto_assign_reports(request):
    return None
