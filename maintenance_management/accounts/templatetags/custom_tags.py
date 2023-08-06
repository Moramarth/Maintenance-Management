from decouple import config
from django import template

register = template.Library()


@register.simple_tag()
def profile_group_info(user):
    return user.groups


@register.simple_tag()
def user_authentication(user):
    return user.is_authenticated


@register.simple_tag()
def user_staff_status(user):
    return user.is_staff


@register.simple_tag()
def address_display_for_profile(obj):
    return obj.company.additionaladdressinformation_set.first()


@register.simple_tag()
def address_display_for_company(obj):
    return obj.additionaladdressinformation_set.first()


@register.simple_tag(takes_context=True)
def pagination_parameters(context, **kwargs):
    """
     Preserves active filter options with pagination and removes any empty values

     Returns Encoded URL parameters
     """

    data = context["request"].GET.copy()
    for key, value in kwargs.items():
        data[key] = value

    for key in [key for key, value in data.items() if not value or value == "unknown"]:
        del data[key]

    return data.urlencode()


@register.simple_tag()
def get_google_maps_api_key():
    return config("GOOGLE_MAPS_API_KEY")