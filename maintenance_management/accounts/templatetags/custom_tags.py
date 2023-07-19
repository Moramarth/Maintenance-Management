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
