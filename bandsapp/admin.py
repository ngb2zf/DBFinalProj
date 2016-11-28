from django.contrib import admin
from .models import Events, Bands, Hosts

admin.site.register(Events)
admin.site.register(Bands)
admin.site.register(Hosts)