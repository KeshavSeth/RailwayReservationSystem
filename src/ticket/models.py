from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime
from trains.models import *
from route.models import *


class Ticket(models.Model):
    holderName = models.CharField(_("Passenger Name"), max_length=255)
    seat = models.OneToOneField(Seat)
    fare = models.PositiveIntegerField(_("Ticket Fare"), default=0)
    #bookedBy = models.ForeignKey(User, max_length=255)
    date = models.DateField(
        _("Date of departure"), default=timezone.now)

    def __str__(self):
        return str(self.id) + " " + str(self.holderName)


class Passenger(models.Model):
    ticket = models.OneToOneField(Ticket)
    name = models.CharField(_("Name of Passenger"), max_length=100)
    #dob = models.DateField(_("Date of Birth "), default=datetime.date(datetime.now()))
    age = models.PositiveIntegerField(_("Age"), default=None)
    sex = models.CharField(_("Gender"), max_length=2)
    birthPreference = models.CharField(_("Birth Preference"), max_length=2)
    foodPreference = models.CharField(_("Food Preference"), max_length=1)
    senior = models.BooleanField(_("Senior Citizen"), default=False)

    def __str__(self):
        return self.name
