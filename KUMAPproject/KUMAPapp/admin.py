from django.contrib import admin
from .models import Building, Entrance, Facility

# Register your models here.
# admin.site.register(Building)
# admin.site.register(Entrance)


class EntranceAdmin(admin.ModelAdmin):
    # fields = ['entrance_name']
    list_display = [ 'building_id','entrance_name', 'entrance_num']

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['building_name', 'building_lat', 'building_lon']
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['building_id',  'category','facility_name','facility_loc']

admin.site.register(Building, BuildingAdmin)
admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Facility, FacilityAdmin)