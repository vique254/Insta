# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-16 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.TextField(max_length=100),
        ),
    ]
