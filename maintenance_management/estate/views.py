from django.shortcuts import render
from django.views import generic as views

from maintenance_management.estate.models import Building


# Create your views here.
class ShowAllBuildings(views.ListView):
    template_name = 'estate/show_all_buildings.html'
    model = Building


class ShowBuildingDetails(views.DetailView):
    template_name = 'estate/building_details.html'
    model = Building
