# -*- coding: utf-8 -*-
from easy_thumbnails.files import get_thumbnailer


# TODO: удалить директорию
def del_imgs__pre_delete(sender, instance, **kwargs):
    '''
    Удаление иображений перед удалением модели.
    В модели должна быть определена функция "get_images_fields()"
    '''
    images_fields = instance.get_images_fields()
    for img in images_fields:
        get_thumbnailer(img).delete_thumbnails()
        img.delete(save=False)



def del_imgs__pre_save(sender, instance, **kwargs):
    '''
    Удаление иображений перед изменением модели.
    В модели должна быть определена функция "get_images_fields()"
    '''
    try:
        this_images = sender.objects.get(id=instance.id).get_images_fields()
        instance_images = instance.get_images_fields()

        for this_img, inst_img in zip(this_images, instance_images):
            if this_img != inst_img:
                get_thumbnailer(this_img).delete_thumbnails()
                this_img.delete(save=False)

    except sender.DoesNotExist:
        pass