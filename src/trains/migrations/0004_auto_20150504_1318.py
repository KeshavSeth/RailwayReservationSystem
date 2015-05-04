# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_auto_20150504_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bogey',
            name='fare',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='train',
        ),
    ]
