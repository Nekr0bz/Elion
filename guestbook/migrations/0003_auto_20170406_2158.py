# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20170308_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='parent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guestbook.GuestBook'),
        ),
    ]
