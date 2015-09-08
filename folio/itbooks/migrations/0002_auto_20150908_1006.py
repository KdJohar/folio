# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='getbook',
            name='title',
            field=models.CharField(unique=True, max_length=250),
        ),
    ]
