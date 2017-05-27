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


def authors(request):
    # author_list = Author.male_authors.all()
    # author_list = Author.sex_manager.reverse()
    # author_list = Author.new_sex_manager.all().male_list()
    author_list = Author.new_sex_manager.male_list()
    return render(request, 'authors.html', locals())

