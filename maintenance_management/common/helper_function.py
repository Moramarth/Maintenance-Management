from maintenance_management.clients.models import Review
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building


def get_queries_as_list():
    all_tenants = list(Company.objects.all())
    all_buildings = list(Building.objects.all())
    all_reviews = list(Review.objects.all())
    return all_tenants, all_buildings, all_reviews


def verify_constants(query, constant):
    """ verifies that we have enough objects to display """
    if len(query) < constant:
        constant = len(query)
    return constant
