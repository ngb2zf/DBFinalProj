from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context
from bandsapp.models import Bands

# Create your views here.

def index(request):
	template = loader.get_template('bandsearch_template.html')
	return HttpResponse(template.render())


def search(request):
	# this is where the query gets executed

	# this is just get variables named in bandsearch_template
    name = request.GET['q']

    # this is where yuo make sql queries and grab the data you want
    found = get_object_or_404(Bands, b_name__iexact=name)

    # we should do something in this loop to put into the context below	
    for f in found:
    	print(f)
    template = loader.get_template('bandresults_template.html')

    # variables are set to be rendered then passed to bandresults_template and displayed
    context = Context({ 'band_name': name,})
    return HttpResponse(template.render(context))
