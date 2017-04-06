# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic.dates import ArchiveIndexView
from django.core.urlresolvers import reverse_lazy
from .models import GuestBook
from .forms import GuestBookForm


class GuestBookView(ArchiveIndexView):
    model = GuestBook
    template_name = 'guestbook/index.html'
    date_field = 'datetime'
    allow_empty = True
    form = None
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = GuestBookForm()
        return super(GuestBookView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestBookView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form_data = {
                'usr': request.user.id,
                'text': request.POST['text'].encode('utf-8')
            }
            self.form = GuestBookForm(form_data)
            if self.form.is_valid():
                self.form.save()
                return redirect(reverse_lazy('guestbook'))

        return super(GuestBookView, self).get(request, *args, **kwargs)