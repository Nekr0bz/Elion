# Установка и настройка
### Требования
Необходимо, чтобы в системе был установлен `pytohn 2.7`.

Подразумевается, что в системе установлен свежий `pip`.
### Установка
Получем исходный код проекта:
```sh
$ git clone https://github.com/Nekr0bz/Elion.git
```
**Для работы проекта необходимо:** 
1) Установить дополнительные модули, перечисленные в файле `requirements.txt`:
```sh
$ pip install -r requirements.txt
```
2) Переместить содержимое директории [Elion-vendors](https://github.com/Nekr0bz/Elion-vendors) в папку проекта.
### База данных
Создаем базу данных на SQLite:
```sh
$ python manage.py migrate
```
Создаем супер-пользователя:
```sh
$ python manage.py createsuperuser
```
### Запуск
Теперь должно работать:
```sh
$ python manage.py runserver
```
### Настройка
Для работоспособности формы отправки сообщений на электронную почту, необходимо в файле `Elion/settings.py` 
настроить SMTP бекенд, который установлен по умолчанию 
([см. документацию](https://docs.djangoproject.com/en/1.10/topics/email/#smtp-backend)).