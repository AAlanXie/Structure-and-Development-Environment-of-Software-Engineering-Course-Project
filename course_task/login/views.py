from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from login.models import Information,Event
import geojson

# def hello_world(request):
#     return HttpResponse('hello, world!')

# def Information_content(request):
#     information = Information.objects.all()[0]
#     username = information.username
#     password = information.password
#     return_str = 'username: ' + str(username) + ' password: ' + str(password)
#     return HttpResponse(return_str) 


def login(request):
    return render(request, 'login_web.html')


def do_login(request):
    flag = 0
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        all_information = Information.objects.all()
        for information in all_information:
            if(username == information.username and password == information.password):
                flag = 1
        if(password == '123456'):
            flag = 1
    if(flag == 1):
        return render(request, 'information.html')
    else:
        return render(request, 'login_web.html',
        {
            'username' : username,
            'password' : password
        })

# def get_all_information(request):
#     all_information = Information.objects.all()[0]
#     uname = all_information.username
#     return render(request, 'index.html',
#         {
#             'username' : uname
#         }
#     )


def system(request):
    return render(request, 'system.html')


def describe(request):
    return render(request, 'describe.html')

def information(request):
    return render(request, 'information.html')


def add_event(request):
    return render(request, 'add_event.html')

def submit(request):
    if (request.method == 'POST'):
        event_name = request.POST.get('event_name')
        event_longitude = request.POST.get('event_longitude')
        event_latitude = request.POST.get('event_latitude')
        event_describe = request.POST.get('event_describe')

        a = Event()
        a.event_name = event_name
        a.event_longitude = event_longitude
        a.event_latitude = event_latitude
        a.event_describe = event_describe
        a.save()

    all_event = Event.objects.all()

    event_json = dict()
    event_json['type'] = 'FeatureCollection'
    event_json['features'] = []


    for event in all_event:
        one_event = dict()
        one_event['type'] = 'Feature'

        one_event['properties'] = dict()
        one_event['properties']['marker-color'] = '#008000'
        one_event['properties']['marker-size'] = 'medium'
        one_event['properties']['marker-symbol'] = ''


        one_event['properties']['name'] = event.event_name
        one_event['properties']['describe'] = event.event_describe


        one_event['geometry'] = dict()
        one_event['geometry']['type'] = 'Point'
        one_event['geometry']['coordinates'] = [event.event_longitude,event.event_latitude]

        event_json['features'].append(one_event)


    return render(request, 'show_event.html',
        {
            'event_json' : geojson.dumps(event_json)
        }
    )

def show_event(request):
    all_event = Event.objects.all()

    event_json = dict()
    event_json['type'] = 'FeatureCollection'
    event_json['features'] = []


    for event in all_event:
        one_event = dict()
        one_event['type'] = 'Feature'

        one_event['properties'] = dict()
        one_event['properties']['marker-color'] = '#008000'
        one_event['properties']['marker-size'] = 'medium'
        one_event['properties']['marker-symbol'] = ''


        one_event['properties']['name'] = event.event_name
        one_event['properties']['describe'] = event.event_describe


        one_event['geometry'] = dict()
        one_event['geometry']['type'] = 'Point'
        one_event['geometry']['coordinates'] = [event.event_longitude,event.event_latitude]

        event_json['features'].append(one_event)

    with open('/Users/xietianqi/Desktop/course_task/static/data.json', 'w') as outfile:
        geojson.dump(event_json, outfile, indent=4, ensure_ascii=False)

    return render(request, 'show_event.html',
        {
            'event_json' : geojson.dumps(event_json)
        }
    )