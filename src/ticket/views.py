from django.shortcuts import render
from ticket.models import *


def book_ticket(request, train_id, coach_id):
    print "function"
    print train_id, coach_id
    return render(request, 'book.html')
