# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourValuesCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name=b'\xd0\xa7\xd0\xb8\xd1\x81\xd0\xbb\xd0\xbe')),
                ('desc1', models.CharField(max_length=20, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('desc2', models.CharField(max_length=20, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='StaticDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_company_opening', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xbe\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f \xd1\x84\xd0\xb8\xd1\x80\xd0\xbc\xd1\x8b')),
                ('history', models.TextField(verbose_name=b'\xd0\x98\xd1\x81\xd1\x82\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('mission', models.TextField(verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbb\xd1\x8c (\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f) \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('mission_img', models.ImageField(help_text=b'470x167px', upload_to=b'about/', verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbb\xd1\x8c (\xd0\xbc\xd0\xb8\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f) \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
                ('description_services', models.TextField(verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3')),
                ('who_we_are1', models.TextField(verbose_name=b'"\xd0\x9a\xd1\x82\xd0\xbe \xd0\xbc\xd1\x8b?" - \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb0\xd0\xb1\xd0\xb7\xd0\xb0\xd1\x86')),
                ('who_we_are2', models.TextField(verbose_name=b'"\xd0\x9a\xd1\x82\xd0\xbe \xd0\xbc\xd1\x8b?" - \xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb9 \xd0\xb0\xd0\xb1\xd0\xb7\xd0\xb0\xd1\x86')),
                ('value_company', models.TextField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8')),
            ],
            options={
                'db_table': 'StaticDates',
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435',
            },
        ),
        migrations.AddField(
            model_name='fourvaluescompany',
            name='parent_static_dates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.StaticDates'),
        ),
    ]
