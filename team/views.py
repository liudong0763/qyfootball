from django.shortcuts import render
from .models import Team
from django.http import HttpResponse


# Create your views here.
def teams(request, area):
    # print(request.META['SERVER_NAME'])
    teams_list = Team.objects.all()
    # return HttpResponse('hello my boy')
    print(teams_list.query)
    return render(request, 'teams.html', locals())


def team(request, area, team_id):

    the_team = Team.objects.get(pk=team_id)

    return render(request, 'team.html', locals())
