# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislature', '0002_auto_20140910_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='medium',
            name='image',
            field=models.ImageField(null=True, upload_to=b'medium', blank=True),
            preserve_default=True,
        ),
    ]
