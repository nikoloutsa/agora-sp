# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-17 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20171017_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.ServiceArea'),
        ),
    ]
