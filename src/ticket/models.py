from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from trains.models import *

# Create your models here.


class Ticket(models.Model):

    """docstring for Ticket"""
    train = models.ForeignKey(Train, default=0)
    trainClass = models.OneToOneField(TrainClass, default=0)
    holderName = models.CharField(_("Passenger Name"), max_length=255)
    seat = models.IntegerField(_("Seat no."), default=0)
    # bookedBy = models.ForeignKey(User, max_length=255)
    date = models.DateField(
        _("Date of departure"), default=datetime.date(datetime.now()))

    def __str__(self):
        return str(self.id) + " " + str(self.holderName)
