# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20150504_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='fare',
            field=models.PositiveIntegerField(default=0, verbose_name='Ticket Fare'),
        ),
    ]
