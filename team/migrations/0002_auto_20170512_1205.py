# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='联系电话'),
        ),
    ]
