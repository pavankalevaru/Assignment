# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 11:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_auto_20190312_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
