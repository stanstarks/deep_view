# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0002_auto_20161023_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modification',
            old_name='image',
            new_name='dataset',
        ),
    ]
