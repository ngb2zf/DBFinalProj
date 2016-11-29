from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context
from bandsapp.models import Bands
import geocoder

# Create your views here.

def index(request):
	template = loader.get_template('bandsearch_template.html')
	return HttpResponse(template.render())


def search(request):
	# this is where the query gets executed

	# this is just get variables named in bandsearch_template
    address = request.GET['address']

    g = geocoder.google(address)
    lat, lon = g.latlng

    price_dir = request.GET['price_dir']

    if price_dir == 'ASC':
    	query = "select * from bandsapp_bands where b_lat > " + str(lat-1) + " and b_lat < " + str(lat+1) + " and b_lon > " + str(lon-1) + " and b_lon < " + str(lon+1) + " order by b_price;"
    else:
    	query = "select * from bandsapp_bands where b_lat > " + str(lat-1) + " and b_lat < " + str(lat+1) + " and b_lon > " + str(lon-1) + " and b_lon < " + str(lon+1) + " order by b_price desc;"


    print(query)

    bands = Bands.objects.raw(query)

    template = loader.get_template('bandresults_template.html')

    # variables are set to be rendered then passed to bandresults_template and displayed
    context = Context({ 'bands': bands })
    return HttpResponse(template.render(context))
