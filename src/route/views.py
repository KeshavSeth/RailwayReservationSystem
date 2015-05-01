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


def get_route_by_station(station_id, date):
    sched = StationSchedule.objects.get_schedule_by_date(station_id, date)
    temp = Route.objects.get_route_by_schedule(sched)
    route = []
    for i in temp:
        route.append(i['id'])
    return route


def find_routes(source, destination, date):
    source_id = Station.objects.get_station_id(source)
    destination_id = Station.objects.get_station_id(destination)
    finalRoute = []
    sourceRoutes = get_route_by_station(source_id, date)
    for i in sourceRoutes:
        x = Route.objects.values('schedule__station').filter(id=i)
        if {'schedule__station': destination_id} in x:
            finalRoute.append(i)
    return finalRoute
