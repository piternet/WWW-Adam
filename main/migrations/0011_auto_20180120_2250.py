# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180120_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to='main/static/main/imgs/'),
        ),
    ]
