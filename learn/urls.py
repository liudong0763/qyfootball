from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^form', views.form, name='form'),
    url(r'^authors', views.authors, name='authors'),
]
