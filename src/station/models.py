from django.db import models
from django.utils.translation import gettext_lazy as _


class StationManager(models.Manager):

    def get_station_name(self, station_id):
        return Station.objects.values().get(id=station_id)['stationName']


class Station(models.Model):
    stationName = models.CharField(_("Station Name"), max_length=255)
    objects = StationManager()

    def __str__(self):
        return self.stationName
