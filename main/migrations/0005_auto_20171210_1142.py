# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171209_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
    ]