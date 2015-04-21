# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20150417_2227'),
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
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 21), verbose_name='Date of departure'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='ticket',
            field=models.ForeignKey(to='ticket.Ticket'),
        ),
    ]
