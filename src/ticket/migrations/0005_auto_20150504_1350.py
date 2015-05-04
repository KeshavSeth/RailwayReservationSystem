# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
        ('ticket', '0004_ticket_fare'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='boardFrom',
            field=models.ForeignKey(related_name='boardfrom', default=1, to='station.Station'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='boardTill',
            field=models.ForeignKey(related_name='boardto', default=1, to='station.Station'),
            preserve_default=False,
        ),
    ]
