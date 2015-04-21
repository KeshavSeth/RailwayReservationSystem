# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0006_auto_20150421_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5, verbose_name='Seat No.')),
                ('available', models.BooleanField(default=False, verbose_name='Booked')),
                ('seatType', models.CharField(max_length=2, verbose_name='Berth Type')),
                ('coach', models.ForeignKey(to='trains.TrainClass')),
                ('train', models.ForeignKey(to='trains.Train')),
            ],
        ),
    ]
