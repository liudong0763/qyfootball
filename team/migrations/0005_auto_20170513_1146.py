# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 03:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170512_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='领队'),
        ),
    ]