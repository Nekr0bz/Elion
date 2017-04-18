# -*- coding: utf-8 -*-
from django.forms import models


class ModelAndOtherLabelChoiceIterator(models.ModelChoiceIterator):
    def __iter__(self):
        for i in super(ModelAndOtherLabelChoiceIterator, self).__iter__():
            yield i

        if self.field.other_label is not None:
            yield (self.field.other_val, self.field.other_label)

    def __len__(self):
        length = super(ModelAndOtherLabelChoiceIterator, self).__len__()
        return length + (1 if self.field.last_label is not None else 0)


class ModelAndOtherLabelChoiceField(models.ModelChoiceField):
    """Расширяет класс ModelChoiceField добавляя произвольное значение в choices"""
    def __init__(self, queryset, other_label='Other', other_val='0', *args, **kwargs):
        self.other_label = other_label
        self.other_val = other_val
        super(ModelAndOtherLabelChoiceField, self).__init__(queryset, *args, **kwargs)

    def _get_choices(self):
        """Функция переопределена, чтобы использовалось ExtModelChoiceIterator"""
        if hasattr(self, '_choices'):
            return self._choices
        return ModelAndOtherLabelChoiceIterator(self)

    choices = property(_get_choices, models.ChoiceField._set_choices)

    def to_python(self, value):
        if value == self.other_val:
            return value
        else:
            return super(ModelAndOtherLabelChoiceField, self).to_python(value)
