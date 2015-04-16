# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_auto_20150414_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('holderName', models.CharField(max_length=255, verbose_name='Passenger Name')),
                ('seat', models.IntegerField(default=0, verbose_name='Seat no.')),
                ('date', models.DateField(default=datetime.date(2015, 4, 14), verbose_name='Date of departure')),
                ('train', models.ForeignKey(default=0, to='trains.Train')),
                ('trainClass', models.OneToOneField(default=0, to='trains.TrainClass')),
            ],
        ),
    ]
