from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchForm


def get_form(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            source = data['source']
            print data
            # TODO
            return HttpResponseRedirect('/display/')
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


def find_trains(request):
    return render(request, 'display.html')
