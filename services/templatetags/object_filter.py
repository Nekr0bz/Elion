# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def filter_type(obj, value):
    """
    Фильтрация списка обьектов по указанному типу
    :param obj: Спиоск обьектов
    :param value: Тип
    :return: Новый список обьектов
    """
    return obj.filter(type=value)