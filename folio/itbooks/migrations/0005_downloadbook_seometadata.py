# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itbooks', '0004_searchtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.OneToOneField(to='itbooks.Book')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
        migrations.CreateModel(
            name='SeoMetaData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('seo_done', models.BooleanField(default=False)),
                ('book', models.OneToOneField(to='itbooks.Book')),
            ],
            options={
                'verbose_name_plural': 'Book Page Metadata',
            },
        ),
    ]
