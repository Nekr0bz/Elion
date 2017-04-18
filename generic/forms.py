# -*- coding: utf-8 -*-
from django.forms import models


class ModelAndOtherLabelsChoiceIterator(models.ModelChoiceIterator):
    def __iter__(self):
        for i in super(ModelAndOtherLabelsChoiceIterator, self).__iter__():
            yield i

        if self.field.other_labels is not None:
            for key in self.field.other_labels:
                yield (key, self.field.other_labels[key])

    def __len__(self):
        length = super(ModelAndOtherLabelsChoiceIterator, self).__len__()
        len_others = len(self.field.other_labels) if self.field.other_labels is not None else 0
        return length + len_others


class ModelAndOtherLabelsChoiceField(models.ModelChoiceField):
    """Расширяет класс ModelChoiceField добавляя словарь с произвольными значениями в choices"""
    def __init__(self, queryset, other_labels, *args, **kwargs):
        self.other_labels = other_labels
        super(ModelAndOtherLabelsChoiceField, self).__init__(queryset, *args, **kwargs)

    def _get_choices(self):
        """Функция переопределена, чтобы использовалось ExtModelChoiceIterator"""
        if hasattr(self, '_choices'):
            return self._choices
        return ModelAndOtherLabelsChoiceIterator(self)

    choices = property(_get_choices, models.ChoiceField._set_choices)

    def to_python(self, value):
        if self.other_labels and value in self.other_labels.keys():
            return value
        else:
            return super(ModelAndOtherLabelsChoiceField, self).to_python(value)
