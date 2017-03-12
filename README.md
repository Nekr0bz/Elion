# Установка и настройка
### Требования
Необходимо, чтобы в системе был установлен `pytohn 2.7`.

Подразумевается, что в системе установлен свежий `pip`.
### Установка
Получем исходный код проекта:
```sh
$ git clone https://github.com/Nekr0bz/Elion.git
```
Для работы проекта необходимо установить дополнительные модули, перечисленные в файле `requirements.txt`:
```sh
$ pip install -r requirements.txt
```
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