# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .forms import ContactMessageForm, SubmitAppForm
from .models import ValuesCompany, Employees, StaticDates


class ContactView(FormView):
    template_name = "about/contact.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        form.send_email()
        success_msg = 'Спасибо, что написали нам. Мы ответим вам в ближайщее время!'
        messages.add_message(self.request, messages.SUCCESS, success_msg)
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.values()[0][0])
        return super(ContactView, self).form_invalid(form)


class SubmitAppView(FormView):
    template_name = "about/submit_app.html"
    form_class = SubmitAppForm
    success_url = reverse_lazy('submit_app')

    def get_initial(self):
        if self.request.user.is_authenticated:
            usr = self.request.user
            initial_dates = {
                'first_name':  usr.first_name,
                'last_name':  usr.last_name,
                'email':  usr.email,
                'phone':  usr.phone_number,
            }
            return initial_dates
        else:
            return super(SubmitAppView, self).get_initial()

    def form_valid(self, form):
        if self.request.user.phone_number != form.cleaned_data['phone']:
            self.request.user.phone_number = form.cleaned_data['phone']
            self.request.user.save()
        form.send_email()
        success_msg = 'Спасибо, что  оставили заявку. Мы перезвоним вам в ближайщее время!'
        messages.add_message(self.request, messages.SUCCESS, success_msg)
        return super(SubmitAppView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.values()[0][0])
        return super(SubmitAppView, self).form_invalid(form)


class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['static_dates'] = StaticDates.objects.all().last()
        context['employees'] = Employees.objects.all()
        context['values_company'] = ValuesCompany.objects.all()
        return context
