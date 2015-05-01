from django.db import models
from django.utils.translation import gettext_lazy as _


class StationManager(models.Manager):

    def get_station_id(self, station_name):
        return Station.objects.values().get(stationName=station_name)['id']


class Station(models.Model):
    stationName = models.CharField(_("Station Name"), max_length=255)
    objects = StationManager()

    def __str__(self):
        return self.stationName
