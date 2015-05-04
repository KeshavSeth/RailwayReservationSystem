from django.shortcuts import render
from ticket.models import *


def book_ticket(request, coach_id):
    print "function"
    print coach_id
    return render(request, 'book.html')
