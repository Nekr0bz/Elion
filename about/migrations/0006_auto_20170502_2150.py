# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20170411_0055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fourvaluescompany',
            options={'verbose_name': '\u0412\u0430\u0436\u043d\u043e \u0447\u0438\u0441\u043b\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', 'verbose_name_plural': '\u0427\u0435\u0442\u044b\u0440\u0435 \u0432\u0430\u0436\u043d\u044b\u0435 \u0446\u0438\u0444\u0440\u044b \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='staticdates',
            name='mission',
            field=models.TextField(verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='staticdates',
            name='value_company',
            field=models.TextField(verbose_name='\u0413\u043e\u0440\u0434\u043e\u0441\u0442\u044c \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
    ]
