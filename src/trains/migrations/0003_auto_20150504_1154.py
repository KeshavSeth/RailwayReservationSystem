# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_trainclass_fare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bogey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=255, verbose_name='Seat Class')),
                ('seatQuota', models.CharField(max_length=255, verbose_name='Seat Quota')),
                ('fare', models.PositiveIntegerField(default=0, verbose_name='Fare')),
            ],
        ),
        migrations.RemoveField(
            model_name='trainclass',
            name='className',
        ),
        migrations.RemoveField(
            model_name='trainclass',
            name='fare',
        ),
        migrations.RemoveField(
            model_name='trainclass',
            name='seatQuota',
        ),
        migrations.AddField(
            model_name='trainclass',
            name='bogey',
            field=models.ForeignKey(default=1, to='trains.Bogey'),
            preserve_default=False,
        ),
    ]
