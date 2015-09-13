# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itbooks', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
