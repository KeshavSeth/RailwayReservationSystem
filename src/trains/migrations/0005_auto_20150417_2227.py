# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0004_auto_20150414_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='trainNumber',
            field=models.CharField(max_length=6, serialize=False, verbose_name='Train Number', primary_key=True),
        ),
    ]
