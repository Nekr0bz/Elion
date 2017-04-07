# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import GuestBook
from .forms import GuestBookForm


class GuestBookIndexView(ArchiveIndexView):
    model = GuestBook
    template_name = 'guestbook/index.html'
    date_field = 'datetime'
    allow_empty = True
    form = None
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = GuestBookForm()
        return super(GuestBookIndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestBookIndexView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            guestbook_id = kwargs.get('guestbook_id', None)
            parent_id = get_object_or_404(GuestBook, id=guestbook_id).id if guestbook_id else None
            form_data = {
                'parent': parent_id,
                'usr': request.user.id,
                'text': request.POST['text'].encode('utf-8')
            }
            self.form = GuestBookForm(form_data)
            if self.form.is_valid():
                self.form.save()
                return redirect(self.request.META.get('HTTP_REFERER', '/'))

        return super(GuestBookIndexView, self).get(request, *args, **kwargs)


class GuestBookDeleteView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get(self, request, *args, **kwargs):
        guestbook = get_object_or_404(GuestBook, id=kwargs['guestbook_id'])

        if guestbook.usr == request.user or request.user.has_perm('guestbook.delete_guestbook'):
            guestbook.delete()
            success_msg = 'Ваш отзыв успешно удалён!'
            messages.add_message(self.request, messages.SUCCESS, success_msg)

        return super(GuestBookDeleteView, self).get(self, request, *args, **kwargs)


class GuestBookUpdateView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def post(self, request, *args, **kwargs):
        guestbook = get_object_or_404(GuestBook, id=kwargs['guestbook_id'])

        if guestbook.usr == request.user or request.user.has_perm('guestbook.change_guestbook'):
            guestbook.text = request.POST['text'].encode('utf-8')
            guestbook.save()

        return super(GuestBookUpdateView, self).post(self, request, *args, **kwargs)

