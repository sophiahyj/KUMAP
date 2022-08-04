from django.contrib import admin
from .models import Building, Entrance, Facility

# Register your models here.
admin.site.register(Building)
admin.site.register(Entrance)
admin.site.register(Facility)