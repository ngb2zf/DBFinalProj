"""DBFinalProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^bands/', include('bandsapp.urls')),
    url(r'^admin/', admin.site.urls),
    # user auth urls
    url(r'^accounts/login/$',  views.login, name='login'),
    url(r'^accounts/auth/$',  views.auth_view, name='auth'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid'),
    url(r'^accounts/register/$', views.register_user, name='register'),
    url(r'^accounts/register_success/$', views.register_success, name='reg_success'),
    url(r'^accounts/register_event_success/$', views.register_event_success, name='reg_event_success'),
    url(r'^accounts/event_delete_success/$', views.event_delete_success, name='event_delete_success'),
    url(r'^accounts/register_band/$', views.register_band, name='reg_band'),
    url(r'^accounts/register_host/$', views.register_host, name='reg_host'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/register_event/$', views.register_event, name='reg_event'),
    url(r'^accounts/not_loggedin/$', views.not_loggedin, name='not_loggedin'),
    url(r'^accounts/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^accounts/host_edit_profile/$', views.host_edit_profile, name='host_edit_profile'),
    url(r'^events/delete/$', views.delete_event, name='host_edit_profile'),


]
