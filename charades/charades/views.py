"""Controls the data that is passed to the webpages"""
from django.shortcuts import render
from strings import actor_instructions, viewer_instructions
from actor import Actor
from viewer import Viewer


##Global variables that will later be added to Game.py
#pylint: disable=invalid-name
actor_user = None
#pylint: disable=invalid-name
viewers_list = []


def index(request):
    return render(request, 'index.html')

def instructions(request):
    """
    The view for the instructions.html page.
    Access the session id, and user type from the request header.
    Selects the correct instructions based on the user type.
    """
    sess_id = 'Not found'
    if 'session_id' in request.GET:
        sess_id = request.GET['session_id']
    instructions_str = ''
    is_actor = False
    if 'user_type' in request.GET:
        user = request.GET['user_type']
        if user == 'Actor':
            instructions_str = actor_instructions()
            is_actor = True
            #pylint: disable=unused-variable, redefined-outer-name
            actor_user = Actor()
        elif user == 'Viewer':
            instructions_str = viewer_instructions()
            viewers_list.append(Viewer())

    return render(request, 'instructions.html', {'session_id' : sess_id,
                                                 'instructions' : instructions_str,
                                                 'actor' : is_actor})
