# -*- coding: utf-8 -*-
from django.db import models


class AreasWork(models.Model):
    region = models.CharField(verbose_name='Регион', max_length=30)

    class Meta:
        db_table = 'AreasWork'
        verbose_name = 'Регион обслуживания'
        verbose_name_plural = 'Регионы обслуживания'

    def __unicode__(self):
        return self.region
