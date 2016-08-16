# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_text', models.CharField(max_length=200)),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(verbose_name='date added')),
                ('likes', models.IntegerField(default=0)),
                ('song_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wavesApp.Genre')),
            ],
        ),
    ]
