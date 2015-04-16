# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('stationID', models.IntegerField(serialize=False, verbose_name='Station ID Number', primary_key=True)),
                ('stationName', models.CharField(max_length=255, verbose_name='Station Name')),
            ],
        ),
    ]
