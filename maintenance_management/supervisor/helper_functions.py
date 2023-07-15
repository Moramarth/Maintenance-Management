from maintenance_management.clients.models import ServiceReport
from maintenance_management.supervisor.models import Assignment


def create_assignment_object(request_user, report, user) -> None:
    """ Creates assignment instance and saves it in the database"""
    Assignment.objects.create(
        service_report=report,
        user=user,
        assigned_by=request_user,
        meeting_required=False,
        expense_estimate_available=False,
    )


def choice_population(query_set):
    """ Converts a query set into a list of tuples, so it can be used in Choice fields"""
    choices = list()
    for item in query_set:
        choices.append((item.pk, item))
    return choices


def report_is_assigned(report, user):
    report.report_status = ServiceReport.ReportStatus.ASSIGNED
    report.assigned_to = user
    report.save()
