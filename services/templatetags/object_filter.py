from django import template

register = template.Library()


@register.filter
def filter_type(obj, value):
    return obj.filter(type=value)