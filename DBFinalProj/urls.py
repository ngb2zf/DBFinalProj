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
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    # user auth urls
    url(r'^accounts/login/$',  views.login, name='login'),
    url(r'^accounts/auth/$',  views.auth_view, name='auth'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid'),
    url(r'^accounts/register/$', views.register_user, name='register'),
    url(r'^accounts/register_success/$', views.register_success, name='reg_success'),



]
