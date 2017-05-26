# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.base import RedirectView
from django.contrib import messages
from .models import GuestBook
from .forms import GuestBookForm


class GuestBookIndexView(ArchiveIndexView):
    """
    Представление отвечающее за 
    отображение списка отзывов
    """
    model = GuestBook
    template_name = 'guestbook/index.html'
    date_field = 'datetime'
    allow_empty = True
    form = None
    paginate_by = 10
    queryset = GuestBook.objects.filter(parent=None)

    def get(self, request, *args, **kwargs):
        """
        Вызывается при GET запросе
        Инициализирует форму
        :param request: Экземпляр запроса
        :return: Страница отзывов
        """
        self.form = GuestBookForm()
        return super(GuestBookIndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Отвечает за данные контекста, 
        которые будут исопльзованы в шаблоне
        :return: Словарь данных контекста
        """
        context = super(GuestBookIndexView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        """
        Вызывается при POST запросе
        Создаёт новый отзыв
        :param request: Экземпляр запроса
        :return: Страница отзывов
        """
        if request.user.is_authenticated:
            guestbook_id = request.POST.get('guestbook_id', None)
            parent_id = get_object_or_404(GuestBook, id=guestbook_id).id if guestbook_id else None
            form_data = {
                'parent': parent_id,
                'usr': request.user.id,
                'text': request.POST['text'].encode('utf-8')
            }
            self.form = GuestBookForm(form_data)
            if self.form.is_valid():
                self.form.save()
                if not parent_id:
                    return redirect(reverse_lazy('guestbook:index'))

        return self.get(request, *args, **kwargs)


class GuestBookDeleteView(RedirectView):
    """
    Представление отвечающее 
    за удаление отзывов
    """
    def get_redirect_url(self, *args, **kwargs):
        """
        Возвращает URL предыдущей страницы
        """
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def post(self, request, *args, **kwargs):
        """
        Вызывается при POST запросе
        Удаляет отзыв
        :param request: Экземпляр запроса
        :return: Страница отзывов
        """
        if self.request.is_ajax():
            try:
                guestbook = GuestBook.objects.get(id=kwargs['guestbook_id'])
                if guestbook.usr == request.user or request.user.has_perm('guestbook.delete_guestbook'):
                    guestbook.delete()
                    success_msg = 'Ваш отзыв успешно удалён!'
                    # TODO: БАГ! появляется только после обновления страницы
                    messages.add_message(self.request, messages.SUCCESS, success_msg)
                    data = {'status': 'ok'}
                else:
                    data = {
                        'status': 'error',
                        'code': 'PermissionDenied',
                        'message': 'У пользователя нету прав на удаление этого объекта.'
                    }

            except GuestBook.DoesNotExist:
                data = {
                    'status': 'error',
                    'code': 'ObjectDoesNotExist',
                    'message': 'Не правильный идентификатор объекта.'
                }
            return JsonResponse(data)

        else:
            return super(GuestBookDeleteView, self).get(self, request, *args, **kwargs)


class GuestBookUpdateView(RedirectView):
    """
    Преставление отвечающее 
    за изменение отзывов
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        Возвращает URL предыдущей страницы
        """
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def post(self, request, *args, **kwargs):
        """
        Вызывается при POST запросе
        Изменяет отзыв
        :param request: Экземпляр запроса
        :return: Страница отзывов
        """
        if self.request.is_ajax():
            try:
                guestbook = GuestBook.objects.get(id=kwargs['guestbook_id'])
                if guestbook.usr == request.user or request.user.has_perm('guestbook.change_guestbook'):
                    guestbook.text = request.POST['text'].encode('utf-8')
                    guestbook.save()
                    data = {'status': 'ok'}
                else:
                    data = {
                        'status': 'error',
                        'code': 'PermissionDenied',
                        'message': 'У пользователя нету прав на изменение этого объекта.'
                    }

            except GuestBook.DoesNotExist:
                data = {
                    'status': 'error',
                    'code': 'ObjectDoesNotExist',
                    'message': 'Не правильный идентификатор объекта.'
                }
            return JsonResponse(data)

        else:
            return super(GuestBookUpdateView, self).get(self, request, *args, **kwargs)

