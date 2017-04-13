from django import template
from Elion import settings

register = template.Library()


@register.simple_tag
def remote_static(path):
    host = settings.ALLOWED_HOSTS[-1]
    return 'http://'+host+'/static/'+path
