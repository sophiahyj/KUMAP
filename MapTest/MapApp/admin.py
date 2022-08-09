from atexit import register
from django.contrib import admin
from MapApp.models import Building, Entrance, Facility

# Register your models here.
admin.site.register(Building)
admin.site.register(Entrance)
admin.site.register(Facility)