__author__ = 'rjd9se'
from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

