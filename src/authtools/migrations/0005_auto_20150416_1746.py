# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '0004_auto_20150416_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name', 'email', 'phone_no', 'gender', 'dob', 'aadhar'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='aadhar',
            field=models.CharField(default=1, max_length=12, verbose_name='aadhar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.date(2015, 4, 16), verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='Male', max_length=6, verbose_name='gender'),
            preserve_default=False,
        ),
    ]
