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
    routeIdList = find_routes(source, destination, date)
    trainIdList = []
    trainNameList = []
    arrivalList = []
    departureList = []
    trainClassList = []
    BogeyList = []
    journeyTime = []
    for i in routeIdList:
        trainIdList.append(Route.objects.get_train_id(i))
    for i in trainIdList:
        trainNameList.append(
            Train.objects.values().get(trainNumber=i)['trainName'])
    for i in routeIdList:
        x = Route.objects.filter(
            id=i, schedule__station__stationName=source).values('schedule__arrival')[0]['schedule__arrival']
        y = Route.objects.filter(
            id=i, schedule__station__stationName=destination).values('schedule__departure')[0]['schedule__departure']
        arrivalList.append(x.time())
        departureList.append(y.time())
        journeyTime.append(y.replace(microsecond=0) - x.replace(microsecond=0))
    coachList = {}
    coach = []

    for i in trainIdList:
        trainClassList.append(Train.objects.get_train_class(i))
    print trainClassList
    for i in trainClassList:
        BogeyList.append(Train.objects.get_train_bogeyName(i))
    for i in xrange(len(trainClassList)):
        for j in xrange(len(trainClassList[i])):
            coachList[trainClassList[i][j]] = BogeyList[i][j]
        coach.append(coachList)

    enquiry = zip(trainIdList, trainNameList, routeIdList,
                  arrivalList, departureList, journeyTime, coach)
    print coach
    print enquiry

    return render(request, 'enquiry.html', {'enquiry': enquiry, 'coachList': coachList})
