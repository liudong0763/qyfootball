# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='authordetail',
            options={'verbose_name': '作者详情', 'verbose_name_plural': '作者详情'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版商', 'verbose_name_plural': '出版商'},
        ),
    ]