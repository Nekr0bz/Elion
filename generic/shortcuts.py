# -*- coding: utf-8 -*-
# TODO: Переместить в приложение для нововстей?
def dir_slug_path(instance, filename):
    '''
    Модель должна иметь поле 'slug' и 'DIR_PATH_PREFIX'
    :return: путь хранения файлов
    '''
    return instance.DIR_PATH_PREFIX + instance.slug + '/' + filename

