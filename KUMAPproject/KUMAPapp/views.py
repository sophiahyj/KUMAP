from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.core import serializers
from urllib import response
from django.http import HttpResponse, JsonResponse
import json
# (https://han-py.tistory.com/356 사용법)
from .models import Building, Entrance, Facility

# Create your views here.
def index(request):
    buildingList = Building.objects.all()
    buildings = serializers.serialize('json', Building.objects.all())

    facilityList = Facility.objects.all()
    facilities = serializers.serialize('json', Facility.objects.all())


    return render(request, "index.html", {"buildingList": buildingList, "buildings": buildings, "facilityList": facilityList, "facilities":facilities, })

@csrf_exempt
def category(request, kind):
    print('아아아아ㅏ아아ㅏ아아아ㅏ아아')
    print(kind)
    if kind == 1:
        kind = 'cafe'
    elif kind == 2:
        kind = 'restaurant'
    elif kind == 3:
        kind = 'lounge'
    elif kind == 4:
        kind = 'book_return'
    elif kind == 5:
        kind = 'printer'
        

    if request.method == 'POST':
        facility = serializers.serialize("json", Facility.objects.filter(category = kind))
        hey = json.loads(facility)
        temp = []
        latlng = []
        
        for element in hey:
            if kind == 6:
                temp = serializers.serialize("json", Building.objects.all())
            else:
                temp = serializers.serialize("json", Building.objects.filter(pk = element['fields']['building_id']))
            temp = json.loads(temp)[0]['fields']
            latlng.append((temp['building_lat'], temp['building_lon']))
        response = {
            'latlng': latlng
        }
    return HttpResponse(json.dumps(response))

        

def detail_ajax(request, pk):
    post = Building.objects.get(pk=pk)
    data = {
        'name': post.building_name,
        'pk': pk,
    }
    #print(data)
    return JsonResponse(data)


def search(request):
    buildingList = Building.objects.all()
    return render(request, 'search.html', {'buildingList':buildingList})

def facility(request, building_pk):
    building = Building.objects.get(pk = building_pk)
    facilities = Facility.objects.filter(building_id = building_pk)

    return render(request, 'facility.html', {'building': building, 'facilities': facilities})
