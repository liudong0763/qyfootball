from django.shortcuts import render
from .forms import *


# Create your views here.
def form(request):
    if request.method == 'POST':
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
    else:
        publisher_form = PublisherForm()
        # print(dir(publisher_form))

    return render(request, 'form.html', locals())
