# -*- coding: utf-8 -*-
from django import template
from Elion import settings

register = template.Library()


@register.simple_tag
def remote_static(path):
    """
    Генерирует абсолютную ссылку до файла
    :param path: название фалйа
    :return: URL
    """
    host = settings.ALLOWED_HOSTS[-1]
    if settings.DEBUG:
        return '/static/'+path
    else:
        return 'http://'+host+'/static/'+path