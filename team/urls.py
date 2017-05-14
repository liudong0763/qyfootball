from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<team_id>\d+)', views.team, {'area': '清远'}, name='team'),
    url(r'^', views.teams, {'area': '清远'}, name='teams'),
]
