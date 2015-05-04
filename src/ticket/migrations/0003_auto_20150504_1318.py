# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150501_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='train',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='trainClass',
        ),
        migrations.AlterField(
            model_name='passenger',
            name='ticket',
            field=models.OneToOneField(to='ticket.Ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.OneToOneField(to='trains.Seat'),
        ),
    ]
