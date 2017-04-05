"""Controls the data that is passed to the webpages"""
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from strings import actor_instructions, viewer_instructions, \
                    actor_none, invalid_session
from actor import Actor
from viewer import Viewer
from game import Game
from phrases import get_phrases_from_type, check_phrase

game = None

def index(request):
    warning = ''
    if 'no_actor' in request.GET:
        warning = actor_none()
    if 'invalid_session' in request.GET:
        warning = invalid_session()
    return render(request, 'index.html', {'warning' : warning})

def instructions(request):
    """
    The view for the instructions.html page.
    Access the session id, and user type from the request header.
    Selects the correct instructions based on the user type.
    """
    if 'session_id' not in request.GET:
        return redirect('/?invalid_session=True')
    if request.GET['session_id'] != 'BSW18':
        return redirect('/?invalid_session=True')
    global game
    if game is None:
        game = Game()
    instructions_str = ''
    outbound_url = ''
    if 'user_type' in request.GET:
        user = request.GET['user_type']
        if user == 'Actor':
            instructions_str = actor_instructions()
            user_added = game.add_actor(Actor())
            request.session['user_type'] = 'Actor'
            outbound_url = reverse('select_phrase')
        elif user == 'Viewer':
            instructions_str = viewer_instructions()
            if 'viewer_number' not in request.session:
                viewer_num = game.add_viewer(Viewer())
                request.session['user_type'] = 'Viewer'
                request.session['viewer_number'] = viewer_num
                outbound_url = reverse('guess', args=(viewer_num,))
            else:
                outbound_url = reverse('guess', args=(request.session['viewer_number'],))

    return render(request, 'instructions.html', {'instructions' : instructions_str,
                                                 'outbound_url' : outbound_url})

def guess(request, _):
    return render(request, 'guess.html', {'viewer_number' : request.session['viewer_number']})

def select_phrase(request):
    """
    The view for the select.html page.
    Gets random phrases from the phrases module using
    get_phrases_from_type
    """
    if game.actor is None:
        return redirect('/?no_actor=True')
    return render(request, 'select_phrase.html', {'phrases' : get_phrases_from_type(5, 'ANY')})

def acting(request):
    """
    The default page for the actor while acting out a word/phrase
    """
    if game.actor is None:
        return redirect('/?no_actor=True')
    phrase = game.actor.current_phrase
    ### Select phrase
    if 'phrase' in request.GET:
        phrase = request.GET['phrase']
        if "+" in phrase:
            phrase = phrase.replace("+", " ")
        if check_phrase(phrase):
            game.actor.set_phrase(phrase)
        else:
            raise RuntimeError("Phrase was not recognised as valid.")

    ### Select current word
    current_word_index = game.actor.current_word_index
    if 'current_word_index' in request.GET:
        current_word_index = request.GET['current_word_index']
        try:
            current_word_index = int(current_word_index)
        except RuntimeError:
            raise RuntimeError("Provided integer for current_word_index was not a number")
        if current_word_index < 1 or current_word_index > len(phrase.split()):
            raise RuntimeError("Provided word index %d is not in the range of the word" \
                               " with length %d." % (current_word_index, len(phrase.split)))
        else:
            game.actor.set_word(current_word_index - 1)

    ### Render page
    return render(request,
                  'acting.html',
                  {'num_words' : len(game.actor.current_phrase_word_list),
                   'word_list' : game.actor.current_phrase_word_list,
                   'current_word' : current_word_index})

def reset(request):
    """
    resets the state of the game
    """
    global game
    game = Game()
    if 'user_type' in request.session:
        del request.session['user_type']
    if 'viewer_number' in request.session:
        del request.session['viewer_number']
    return redirect('/')