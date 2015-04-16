# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('trainName', models.CharField(max_length=255, verbose_name='Train Name')),
                ('trainNumber', models.IntegerField(default=0, serialize=False, verbose_name='Train Number', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=255, verbose_name='Seat Class')),
                ('SeatQuota', models.CharField(max_length=255, verbose_name='Seat Quota')),
                ('totalSeats', models.IntegerField(default=0, verbose_name='Total Seats')),
                ('availSeats', models.IntegerField(default=0, verbose_name='Avaiable Seats')),
            ],
        ),
    ]
