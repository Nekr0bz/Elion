# -*- coding: utf-8 -*-
from django import forms

from .models import GuestBook


class GuestBookForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label="Отзыв")

    class Meta:
        fields = ['text', 'usr']
        model = GuestBook
