from django.db import models
from django.utils.translation import gettext_lazy as _
from trains.models import *
from datetime import datetime


class Station(models.Model):
	name = models.CharField(_("Station Name"),max_length=255)

	def __str__(self):
		return self.name

class StationSchedule(models.Model):
	station = models.ForeignKey(Station)
	arrival = models.TimeField(_("Arrival Time"))
	departure = models.TimeField(_("Departure Time"))

	def __str__(self):
		return str(self.station) + " | " + str(self.arrival) + " | " + str(self.departure)


class RouteManager(models.Manager):
	def get_schedule(self,Id):
		schedule = {}
		schedule['arrival'] = Route.objects.values('schedule__arrival').filter(id =Id)
		schedule['departure'] = Route.objects.values('schedule__departure').filter(id =Id)
		schedule['station'] = Route.objects.values('schedule__station').filter(id =Id)
		return schedule

	def get_train_id(self,route_id):
		return Route.objects.values().get(id=route_id)['train_id']
class Route(models.Model):
    date = models.DateField(_("Date of journey"), default=datetime.date(datetime.now()))
    train = models.OneToOneField(Train)
    schedule = models.ManyToManyField(StationSchedule, related_name="stations")
    objects = RouteManager()

    def __str__(self):
    	return str(self.train) + " | " + str(self.date)