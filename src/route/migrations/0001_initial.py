# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 27, 20, 857843), verbose_name='Date of journey')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Station Name')),
            ],
        ),
        migrations.CreateModel(
            name='StationSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival', models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 27, 20, 857236), verbose_name='Arrival Time')),
                ('departure', models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 27, 20, 857291), verbose_name='Departure Time')),
                ('station', models.ForeignKey(to='route.Station')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='schedule',
            field=models.ManyToManyField(related_name='stations', to='route.StationSchedule'),
        ),
        migrations.AddField(
            model_name='route',
            name='train',
            field=models.OneToOneField(to='trains.Train'),
        ),
    ]
