# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5, verbose_name='Seat No.')),
                ('available', models.BooleanField(default=False, verbose_name='Booked')),
                ('seatType', models.CharField(default=b'lower', max_length=2, verbose_name='Berth Type', choices=[(b'LO', b'lower'), (b'MI', b'middle'), (b'UP', b'upper')])),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('trainName', models.CharField(max_length=255, verbose_name='Train Name')),
                ('trainNumber', models.CharField(max_length=6, serialize=False, verbose_name='Train Number', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=255, verbose_name='Seat Class')),
                ('seatQuota', models.CharField(max_length=255, verbose_name='Seat Quota')),
                ('totalSeats', models.IntegerField(default=0, verbose_name='Total Seats')),
                ('availSeats', models.IntegerField(default=0, verbose_name='Avaiable Seats')),
            ],
        ),
        migrations.AddField(
            model_name='train',
            name='coach',
            field=models.ManyToManyField(to='trains.TrainClass'),
        ),
        migrations.AddField(
            model_name='seat',
            name='coach',
            field=models.ForeignKey(to='trains.TrainClass'),
        ),
        migrations.AddField(
            model_name='seat',
            name='train',
            field=models.ForeignKey(to='trains.Train'),
        ),
    ]
