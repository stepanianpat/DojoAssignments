# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailValidation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='email',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=155),
        ),
    ]