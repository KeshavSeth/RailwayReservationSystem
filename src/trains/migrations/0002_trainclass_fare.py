# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainclass',
            name='fare',
            field=models.PositiveIntegerField(default=0, verbose_name='Fare'),
        ),
    ]
