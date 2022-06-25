from django.contrib import admin
from django.urls import path,include
import login.views

urlpatterns = [
    # path('hello_world', login.views.hello_world),
    # path('content', login.views.Information_content),

    path('login_web', login.views.do_login, name = 'check'),
    # path('index', login.views.get_all_information),
    
    path('', login.views.login),
    path('system', login.views.system),
    path('describe', login.views.describe),
    path('information', login.views.information),
    path('add_event', login.views.add_event),
    path('show_event', login.views.show_event),

    path('submit', login.views.submit, name = 'check2'),
]