from django import template

register = template.Library()


@register.filter
def filter_parent(obj):
    return [o for o in obj if not o.parent]