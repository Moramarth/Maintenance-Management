import django_filters

from maintenance_management.estate.models import Building


class BuildingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Search by name")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains", label="Search by city")

    class Meta:
        model = Building
        exclude = ["address", "file", "tenants"]
