# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0003_mazedumper'),
    ]

    operations = [
        migrations.AddField(
            model_name='mazedumper',
            name='cur_node_col',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mazedumper',
            name='cur_node_row',
            field=models.IntegerField(default=0),
        ),
    ]
