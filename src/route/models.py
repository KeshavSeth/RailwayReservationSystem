from django.db import models
from django.utils.translation import gettext_lazy as _
from trains.models import *
from datetime import datetime
from django.utils import timezone
from station.models import *


class ScheduleManager(models.Manager):

    def get_schedule_by_date(self, station_id, date):
        station = StationSchedule.objects.values().filter(station=station_id)
        temp = []
        for i in station:
            if i['departure'].date() == date:
                temp.append(i)
        return temp


class StationSchedule(models.Model):
    station = models.ForeignKey(Station)
    arrival = models.DateTimeField(_("Arrival Time"), default=timezone.now)
    departure = models.DateTimeField(
        _("Departure Time"), default=timezone.now)
    objects = ScheduleManager()

    def __str__(self):
        return str(self.station) + " | " + str(self.arrival) + " | " + str(self.departure)


class RouteManager(models.Manager):

    def get_schedule(self, Id):
        schedule = {}
        schedule['arrival'] = Route.objects.values(
            'schedule__arrival').filter(id=Id)
        schedule['departure'] = Route.objects.values(
            'schedule__departure').filter(id=Id)
        schedule['station'] = Route.objects.values(
            'schedule__station').filter(id=Id)
        return schedule

    def get_train_id(self, route_id):
        return Route.objects.values().get(id=route_id)['train_id']

    def sort_by_arrival(self, schedule):
        # return sorted(Route.objects.get_schedule(route_id)['arrival'],
        # key=lambda k: k['schedule__arrival'])
        x = (schedule)['arrival']
        y = (schedule)['station']
        z = (schedule)['departure']
        # convert station_id to station_name
        for i in y:
            i['schedule__station'] = Station.objects.get_station_name(
                i['schedule__station'])
        indices = sorted(range(len(x)), key=lambda k: x[k])
        arrival = [x[i] for i in indices]
        station = [y[i] for i in indices]
        departure = [z[i] for i in indices]
        return zip(arrival, departure, station)


class Route(models.Model):
    datetime = models.DateTimeField(
        _("Date of journey"), default=timezone.now)
    train = models.OneToOneField(Train)
    schedule = models.ManyToManyField(StationSchedule, related_name="stations")
    objects = RouteManager()

    def __str__(self):
        return str(self.train) + " | " + str(self.datetime)
