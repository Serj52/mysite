# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-17 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210217_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='festival_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Festival'),
        ),
    ]