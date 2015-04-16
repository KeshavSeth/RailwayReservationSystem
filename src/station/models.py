from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Station(models.Model):

    """docstring for Station"""
    stationID = models.IntegerField(_("Station ID Number"), primary_key=True)
    stationName = models.CharField(_("Station Name"), max_length=255)

    def __str__(self):
        return self.stationName
