from django.shortcuts import render
from route.models import *
from station.models import *
from trains.models import *

# Create your views here.


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
