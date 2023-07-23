import django_filters
from django.db.models import Q

from maintenance_management.accounts.enums import GroupEnum
from maintenance_management.clients.models import ServiceReport


class ServiceReportFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr='icontains',
        label="Search in title",
    )

    class Meta:
        model = ServiceReport
        fields = {
            "report_type": ["exact"],
            "report_status": ["exact"],
            "company": ["exact"],
        }


def initial_query_set_service_report_filter(request, queryset):
    """ Provides restricted queryset based on business logic authorization"""
    if request.user.groups.name == str(GroupEnum.supervisor.value):
        return queryset
    elif request.user.groups.name == str(GroupEnum.engineering.value):
        return queryset.filter(
            Q(assigned_to=request.user)
            | Q(report_type=request.user.appuserprofile.expertise)
            | Q(report_type=ServiceReport.ReportType.OTHER)
        )
    return queryset.filter(
        Q(user=request.user)
        | Q(user__appuserprofile__company=request.user.appuserprofile.company)
    )


def first_and_last_name_filter_for_service_report(name, queryset):
    return queryset.filter(
        Q(user__appuserprofile__first_name__icontains=name)
        | Q(user__appuserprofile__last_name__icontains=name)
        | Q(assigned_to__appuserprofile__first_name__icontains=name)
        | Q(assigned_to__appuserprofile__last_name__icontains=name)
    )
