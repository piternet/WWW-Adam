# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_profile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='main/static/main/imgs/'),
        ),
    ]
