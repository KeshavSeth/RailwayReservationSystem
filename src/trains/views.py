from django.shortcuts import render
from route.models import *
from route.views import *
from station.models import *
from trains.models import *


def trainList(request):
    nameList = []
    numberList = []
    train = {}
    trainList = Train.objects.values('trainName', 'trainNumber').all()
    for i in trainList:
        nameList.append(i['trainName'])
        numberList.append(i['trainNumber'])

    train['name'] = nameList
    train['number'] = numberList
    context = {'train': train}
    return render(request, 'train_dashboard.html', context)


def trainEnquiry(request):
    source = request.POST['source']
    destination = request.POST['destination']
    date = request.POST['date']
    print source, destination, date
    routes = find_routes(source, destination, date)
    trainList = []
    for i in routes:
        trainList.append(Route.objects.get_train_id(i))
    return render(request, 'enquiry.html', {'trainList': trainList, 'routeList': routes})
