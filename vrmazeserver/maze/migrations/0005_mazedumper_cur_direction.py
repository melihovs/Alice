# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0004_auto_20151001_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='mazedumper',
            name='cur_direction',
            field=models.CharField(default=b'', max_length=1),
        ),
    ]
