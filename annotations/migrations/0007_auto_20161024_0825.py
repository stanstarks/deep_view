# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0006_auto_20161024_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]