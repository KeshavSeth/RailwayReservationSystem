# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0005_auto_20150417_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainclass',
            name='train',
        ),
        migrations.AddField(
            model_name='train',
            name='coach',
            field=models.ManyToManyField(to='trains.TrainClass'),
        ),
    ]
