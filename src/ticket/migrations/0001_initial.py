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
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name of Passenger')),
                ('age', models.PositiveIntegerField(default=None, verbose_name='Age')),
                ('sex', models.CharField(max_length=2, verbose_name='Gender')),
                ('birthPreference', models.CharField(max_length=2, verbose_name='Birth Preference')),
                ('foodPreference', models.CharField(max_length=1, verbose_name='Food Preference')),
                ('senior', models.BooleanField(default=False, verbose_name='Senior Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('holderName', models.CharField(max_length=255, verbose_name='Passenger Name')),
                ('seat', models.IntegerField(default=0, verbose_name='Seat no.')),
                ('date', models.DateField(default=datetime.date(2015, 4, 28), verbose_name='Date of departure')),
                ('train', models.ForeignKey(default=0, to='trains.Train')),
                ('trainClass', models.OneToOneField(default=0, to='trains.TrainClass')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='ticket',
            field=models.ForeignKey(to='ticket.Ticket'),
        ),
    ]
