from django.shortcuts import render
from django.http import HttpResponseRedirect
from ticket.models import *
from trains.models import *
from .forms import *


def get_availability(request, train_id, coach_id):
    request.session['train_id'] = train_id
    request.session['coach_id'] = coach_id
    print train_id, coach_id

    availSeats = TrainClass.objects.values().get(
        id=coach_id)['availSeats']
    if availSeats <= 0:
        status = 'Sorry! All booked. WaitList is ' + str(w)
    else:
        status = "Available " + str(availSeats) + " seats"
    print availSeats
    return render(request, 'book.html', {'status': status})


def passenger_form(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print data
            return HttpResponseRedirect('/booked/')
    else:
        form = PassengerForm()
    return render(request, 'passenger.html', {'form': form})
