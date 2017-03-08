# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic.dates import ArchiveIndexView
from .models import GuestBook
from .forms import GuestBookForm


class GuestBookView(ArchiveIndexView):
    model = GuestBook
    template_name = 'guestbook/index.html'
    date_field = 'datetime'
    allow_empty = True
    form = None
    # TODO: добавить пагинацию

    def get(self, request, *args, **kwargs):
        self.form = GuestBookForm()
        return super(GuestBookView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestBookView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form_data = {
            'usr': request.user.id,
            'text': str(request.POST['text'].encode('utf-8'))
        }
        print (form_data)
        self.form = GuestBookForm(form_data)
        if self.form.is_valid():
            self.form.save()
            return redirect('guestbook:index')
        else:
            print ('не валидна')
            return super(GuestBookView, self).get(request, *args, **kwargs)