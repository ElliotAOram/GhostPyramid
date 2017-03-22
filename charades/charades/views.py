from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime
from strings import actor_instructions, viewer_instructions 

def index(request):
    return render(request, 'index.html')

def instructions(request):
    sess_id = 'Not found'
    if 'session_id' in request.GET:
        sess_id = request.GET['session_id']
    instructions = ''
    actor = False
    if 'user_type' in request.GET:
        user = request.GET['user_type']
        if user == 'Actor':
            instructions = actor_instructions
            actor = True
        elif user == 'Viewer':
            instructions = viewer_instructions
        
    return render(request, 'instructions.html', {'session_id' : sess_id,
                                                 'instructions' : instructions,
                                                 'actor' : actor})
