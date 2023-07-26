from maintenance_management.common.forms import SearchByNameForm, PaginateByForm
from maintenance_management.estate.models import Building


def context_forms_and_common_queries(request):
    context_data = {
        "buildings": Building.objects.all(),
        "search_by_name_form": SearchByNameForm(request.GET),
        "paginator_form": PaginateByForm(request.GET),
    }
    return context_data
