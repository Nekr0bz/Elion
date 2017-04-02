from django.contrib.admin.forms import AdminAuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.contrib.auth import logout


class LoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


