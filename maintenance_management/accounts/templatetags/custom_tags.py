from django import template

register = template.Library()


@register.simple_tag()
def profile_group_info(user):
    return user.groups.first()


@register.simple_tag()
def address_display(obj):
    return obj.company.additionaladdressinformation_set.first()
