# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itbooks', '0006_auto_20160611_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='downloadbook',
            options={'ordering': ['-download'], 'verbose_name_plural': 'Download'},
        ),
    ]
