from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# from .models import Question, Choice

# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the main bands page.")

