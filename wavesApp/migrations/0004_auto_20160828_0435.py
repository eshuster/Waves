# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wavesApp', '0003_auto_20160828_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='soundcloud_access_token',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
