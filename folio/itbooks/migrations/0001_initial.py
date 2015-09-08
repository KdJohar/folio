# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('isbn', models.CharField(unique=True, max_length=250)),
                ('slug', models.SlugField(unique=True, max_length=250)),
                ('description', models.TextField(null=True)),
                ('image', models.URLField(unique=True, null=True, blank=True)),
                ('publisher', models.CharField(max_length=250, null=True, blank=True)),
                ('author', models.CharField(max_length=250, null=True, blank=True)),
                ('pages', models.CharField(max_length=5, null=True, blank=True)),
                ('language', models.CharField(max_length=100, null=True, blank=True)),
                ('download', models.URLField(unique=True, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('most_downloaded', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='GetBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
