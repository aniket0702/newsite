# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]