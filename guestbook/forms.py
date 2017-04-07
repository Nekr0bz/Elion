# -*- coding: utf-8 -*-
from django import forms

from .models import GuestBook


class GuestBookForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'style': 'width :100%; height: 100px',
        'class': 'form-control',
        'placeholder': 'Напишите ваш отзыв'
    }))

    class Meta:
        fields = ['text', 'usr', 'parent']
        model = GuestBook
