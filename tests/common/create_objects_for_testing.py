from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from maintenance_management.clients.models import ServiceReport, Review
from maintenance_management.common.models import Company
from maintenance_management.estate.models import Building

UserModel = get_user_model()


def create_objects_for_testing(number):
    """
    Creates one group for a placeholder and desired number of objects of classes
    Building, Company, UserModel, ServiceReport and Review

    All objects needed for testing the home page
    """

    Group.objects.create(name="placeholder")
    group_object = Group.objects.first()
    start = len(UserModel.objects.all())
    for i in range(start + 1, start + number + 1):
        UserModel.objects.create(
            email=f"email{i}@test.com",
            password="Te$tP@ssw0rd",
            groups=group_object,
        )
        Building.objects.create(
            name=f"Building {i}",
            city=f"City {i}",
            address=f"Address {i}",
        )
        Company.objects.create(
            name=f"Company {i}"
        )
        ServiceReport.objects.create(
            title=f"Title {i}",
            user=UserModel.objects.get(email=f"email{i}@test.com"),
            company=Company.objects.get(name=f"Company {i}"),
            report_type=ServiceReport.ReportType.OTHER,
        )
        Review.objects.create(
            user=UserModel.objects.get(email=f"email{i}@test.com"),
            service_report=ServiceReport.objects.get(title=f"Title {i}"),
            rating=Review.Rating.TWO
        )
