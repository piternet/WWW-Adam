# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171209_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='main.Tag'),
        ),
    ]
