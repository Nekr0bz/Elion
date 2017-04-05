# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .forms import ContactMessageForm


class ContactView(FormView):
    template_name = "about/contact.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy('contacts')
    # TODO: сообщения об ошибках

    def form_valid(self, form):
        form.send_email()
        success_msg = 'Спасибо, что написали нам. Мы ответим вам в ближайщее время!'
        messages.add_message(self.request, messages.SUCCESS, success_msg)
        return super(ContactView, self).form_valid(form)

