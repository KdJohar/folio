# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itbooks', '0005_downloadbook_seometadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downloadbook',
            old_name='quantity',
            new_name='download',
        ),
    ]
