# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 22:13
from __future__ import unicode_literals

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='address2',
        ),
        migrations.AddField(
            model_name='instrument',
            name='address',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
