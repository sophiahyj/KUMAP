from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.core import serializers
from urllib import response
from django.http import HttpResponse, JsonResponse
import os
import json
# (https://han-py.tistory.com/356 사용법)
from .models import Building, Entrance, Facility
from pathlib import Path
import environ
# django-environ이용해서 환경변수 처리
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Create your views here.
def index(request):
    kakaoKey=env('KAKAO_APP_KEY')
    tmapKey=env('TMAP_APP_KEY')
    buildingList = Building.objects.order_by('building_name')
    buildings = serializers.serialize('json', Building.objects.all())

    facilityList = Facility.objects.all()
    facilities = serializers.serialize('json', Facility.objects.all())


    return render(request, "index.html", {"kakaoKey": kakaoKey, "tmapKey": tmapKey, "buildingList": buildingList, "buildings": buildings, "facilityList": facilityList, "facilities":facilities, })

@csrf_exempt
def category(request, kind):
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
    elif kind == 7:
        kind = 'one-stop' 
        
    #좀더 효율적으로 바꾸기 바보야
    if request.method == 'POST':
        temp = []
        setData = []


        #모든 건물 카테고리 버튼을 클릭했을 때
        if kind == 6:
            facility = serializers.serialize("json", Building.objects.all())
            hey = json.loads(facility)
            for element in hey:
                print(element)
                setData.append((element['pk'], element['fields']['building_name'], element['fields']['building_lat'], element['fields']['building_lon']))
       
        #그 외의 카테고리 버튼을 클릭했을 때
        else:
            facility = serializers.serialize("json", Facility.objects.filter(category = kind))
            hey = json.loads(facility)
            for element in hey:
                temp = serializers.serialize("json", Building.objects.filter(pk = element['fields']['building_id']))
                temp = json.loads(temp)[0]
                setData.append((temp['pk'], temp['fields']['building_name'], temp['fields']['building_lat'], temp['fields']['building_lon']))


        response = {
            # 'latlng': latlng
            'setData':setData
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
    buildingList = Building.objects.order_by('building_name')
    return render(request, 'search.html', {'buildingList':buildingList})

def facility(request, building_pk):
    building = Building.objects.get(pk = building_pk)
    facilities = Facility.objects.filter(building_id = building_pk)

    return render(request, 'facility.html', {'building': building, 'facilities': facilities})

def entrance(request, building_pk):
    kakaoKey=env('KAKAO_APP_KEY')
    buildingslists = Building.objects.get(pk = building_pk)
    entrances = Entrance.objects.filter(building_id = building_pk)
    schoolj = serializers.serialize('json', [Building.objects.filter(pk=building_pk)[0]])
    doorsj = serializers.serialize('json', Entrance.objects.filter(building_id=building_pk))

    return render(request, 'entrance.html', {'kakaoKey':kakaoKey,'buildingslists': buildingslists, 'entrances': entrances, 'schoolj': schoolj, 'doorsj': doorsj})

def first(request):
    return render(request, 'first.html')

@csrf_exempt
def time(request, from_building, to_building):
    from_building = from_building[6:]
    to_building = to_building[6:]
    print(1234, from_building,to_building)
    fromBuilding = Building.objects.get(building_name = from_building)
    toBuilding = Building.objects.get(building_name = to_building)
    data = {
        'frombuilding_lat':str(fromBuilding.building_lat),
        'frombuilding_lon':str(fromBuilding.building_lon),
        'tobuilding_lat':str(toBuilding.building_lat),
        'tobuilding_lon':str(toBuilding.building_lon),
    }
    print(data)
    return JsonResponse(data)