# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 11:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0019_merge_20180412_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAdminship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[['pending', 'Pending'], ['approved', 'Approved'], ['rejected', 'Rejected']], default='pending', max_length=30)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.Service')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='serviceownership',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='serviceownership',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='serviceownership',
            name='service',
        ),
        migrations.DeleteModel(
            name='ServiceOwnership',
        ),
        migrations.AlterUniqueTogether(
            name='serviceadminship',
            unique_together=set([('service', 'admin')]),
        ),
    ]
