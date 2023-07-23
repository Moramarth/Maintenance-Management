from django.views import generic as views

from maintenance_management.estate.filters import BuildingFilter
from maintenance_management.estate.models import Building


class ShowAllBuildings(views.ListView):
    template_name = 'estate/show_all_buildings.html'
    model = Building
    ordering = ["name"]
    filter_set = None

    _DEFAULT_PAGINATE_BY = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter_set = BuildingFilter(self.request.GET, queryset)
        return self.filter_set.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "building_filter_form": self.filter_set.form
        })
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginator", ShowAllBuildings._DEFAULT_PAGINATE_BY)


class ShowBuildingDetails(views.DetailView):
    template_name = 'estate/building_details.html'
    model = Building
