# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0002_delete_mazedumper'),
    ]

    operations = [
        migrations.CreateModel(
            name='MazeDumper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maze_json_dump', models.CharField(max_length=2000)),
            ],
        ),
    ]
