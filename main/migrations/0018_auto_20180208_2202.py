# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_message_readed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(null=True),
        ),
    ]