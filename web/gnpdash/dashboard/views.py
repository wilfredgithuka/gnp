from django.shortcuts import render
from time import gmtime, strftime
import json
import cantools
import can
import threading

##db = cantools.database.load_file('nissan.dbc')
##canbus = can.interface.Bus('vcan0', bustype = "socketcan")

context = {
    'speed': 0,
    'gear': 'P',
    'steering': 0,
    'time': strftime("%I:%M %p", gmtime())
}

def update():
    while True:
        message = canbus.recv()
def canbus(request):
    return Httpresponse(json.dumps(context), content_type='application/json')

def home(request):
    return render(request, 'dash/dash.html', context)
