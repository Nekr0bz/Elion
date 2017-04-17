# -*- coding: utf-8 -*-

import os

try:
    from private_settings import *
except ImportError:
    msg = 'Конфигурации для SMTP скрыты.'
    print (msg)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w*-f#h*y(g0lc+c3%elgef03hlz(#k^!yn8aa1h4p-&o!*!ugo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'nekr0bz.myjino.ru']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'phonenumber_field', 'easy_thumbnails', 'ckeditor', 'ckeditor_uploader',

    'accounts', 'services', 'news', 'guestbook', 'about', 'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Elion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'generic/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Elion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Конфигурации миниатюр

THUMBNAIL_BASEDIR = "thumbnails"
THUMBNAIL_DEFAULT_OPTIONS = {"crop": "smart"}
THUMBNAIL_ALIASES = {
    "for_admin_panel": {"size": (150, 150)},
    "about.StaticDates": {
        "mission": {"size": (470, 167)},
    },
    "about.Employees": {
        "avatar": {"size": (130, 130)},
    },
    "services.Service": {
        "srvc_main": {"size": (730, 305)}
    },
    "services.ServiceSections": {
        "section_srvc": {"size": (248, 199)},
        "section_desc": {"size": (151, 161)}
    },
    "services.FourServiceDirection": {
        "four_srvc": {"size": (154, 142)}
    },
    "news.News": {
        "news_list": {"size": (548, 260)},
        "news_detail": {"size": (1148, 360)},
        "news_main": {"size": (480, 341)},
    }
}


AUTH_USER_MODEL = 'accounts.User'

PHONENUMBER_DB_FORMAT = 'E164'

# Конфигурации wysiwyg-редактора

CKEDITOR_JQUERY_URL = 'http://nekr0bz.myjino.ru/static/vendors/js/JQuery/jquery-3.1.1.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Full': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker'], ['Undo', 'Redo'],
            ['Blockquote', 'HorizontalRule'], ['Link', 'Unlink'], ['Outdent', 'Indent'],
            ['Image', 'TextColor', 'BGColor'], ['Maximize'],
        ],
        'toolbar': 'Full',
        'height': 500,
        'width': 1010,
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
    }
}

try:
    from settings_local import *
except ImportError:
    print ("DEBUG")