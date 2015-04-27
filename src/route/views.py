from django.shortcuts import render
from route.models import *
from station.models import Station
from trains.models import *


def get_route(request,route_id):
	route = Route.objects.get_schedule(route_id)
	trainId = Route.objects.get_train_id(route_id)
	trainName = Train.objects.get_train(trainId)
	arr = []
	dep = []
	sta = []
	arrival = route['arrival']
	departure = route['departure']
	station = route['station']
	for i in arrival:
		arr.append(i['schedule__arrival'])
	for j in departure:
		dep.append(j['schedule__departure'])
	for k in station:
		sta.append(Station.objects.get_station(k['schedule__station']))
	schedule = zip(sta,arr,dep)
	print schedule
	context = {'schedule': schedule, 'trainId': trainId, 'trainName': trainName }
	return render(request, 'route.html', context)


