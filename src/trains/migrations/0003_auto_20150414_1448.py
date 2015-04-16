# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_trainclass_train'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='trainNumber',
            field=models.IntegerField(serialize=False, verbose_name='Train Number', primary_key=True),
        ),
    ]
