from django.shortcuts import render
from route.models import *
from station.models import Station
from trains.models import *


def get_route_by_train(request, train_id):
    name = Train.objects.values().get(trainNumber=train_id)['trainName']
    route_id = Route.objects.values().get(train__trainName=name)['id']
    schedule = Route.objects.get_schedule(route_id)
    route = Route.objects.sort_by_arrival(schedule)
    print route
    context = {'route': route,
               'trainId': train_id, 'trainName': name}
    return render(request, 'route.html', context)


def get_train_by_station(request, station_id, date):
    pass
