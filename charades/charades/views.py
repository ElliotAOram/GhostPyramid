"""Controls the data that is passed to the webpages"""
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from strings import actor_instructions, viewer_instructions, \
                    actor_none, invalid_session, actor_already_defined, \
                    new_phrase, new_word, incorrect_guess, select_word
from actor import Actor
from game import Game
from phrases import get_phrases_from_type, check_phrase

#pylint: disable=invalid-name, global-statement
GAME = None

def index(request):
    warning = ''
    if 'no_actor' in request.GET:
        warning = actor_none()
    if 'invalid_session' in request.GET:
        warning = invalid_session()
    if 'actor_already' in request.GET:
        warning = actor_already_defined()
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
    global GAME
    if GAME is None:
        GAME = Game()

    instructions_str = ''
    outbound_url = ''
    is_actor = False
    phrase_ready = False
    if GAME.actor is not None:
        phrase_ready = GAME.actor.phrase_ready()

    if 'user_type' in request.GET:
        user = request.GET['user_type']
        if user == 'Actor':
            instructions_str = actor_instructions()
            actor_added = GAME.add_actor(Actor())
            if actor_added is False:
                return redirect('/?actor_already')
            request.session['user_type'] = 'Actor'
            outbound_url = reverse('select_phrase')
            is_actor = True
        elif user == 'Viewer':
            instructions_str = viewer_instructions()
            if 'viewer_number' not in request.session:
                viewer_num = GAME.add_viewer()
                request.session['user_type'] = 'Viewer'
                request.session['viewer_number'] = viewer_num
                outbound_url = reverse('guess')
            else:
                outbound_url = reverse('guess')

    return render(request, 'instructions.html', {'instructions' : instructions_str,
                                                 'outbound_url' : outbound_url,
                                                 'is_actor': is_actor,
                                                 'phrase_ready' : phrase_ready})

def guess(request):
    """
    The controller for the viewer guess.html page
    """
    user_guess = ''
    incorrect = ''
    if 'guess' in request.GET:
        user_guess = request.GET['guess']
    if 'guess_type' in request.GET:
        if request.GET['guess_type'] == 'Guess Word':
            if user_guess.upper() == GAME.actor.current_word.upper():
                GAME.set_guess_type(False)
                GAME.set_guess(user_guess)
                GAME.winning_viewer_number = request.session['viewer_number']
                GAME.lookup_viewer(request.session['viewer_number']).increment_points(10)
                GAME.actor.complete_word()
                if len(GAME.actor.completed_words) == len(GAME.actor.current_phrase_word_list):
                    GAME.set_guess_type(True)
                    GAME.actor.phrase_complete()
                return redirect('/waiting_for_actor/')
            else:
                incorrect = incorrect_guess()
        if request.GET['guess_type'] == 'Guess Phrase':
            if user_guess.upper() == GAME.actor.current_phrase.upper():
                GAME.set_guess_type(True)
                GAME.set_guess(user_guess)
                GAME.winning_viewer_number = request.session['viewer_number']
                GAME.lookup_viewer(request.session['viewer_number']).increment_points(20)
                GAME.actor.phrase_complete()
                return redirect('/waiting_for_actor/')
            else:
                incorrect = incorrect_guess()
    outbound_url = reverse('guess')
    return render(request, 'guess.html', {'viewer_number' : request.session['viewer_number'],
                                          'type' : GAME.actor.phrase_genre,
                                          'total_words' : len(GAME.actor.current_phrase_word_list),
                                          'current_word_index' : GAME.actor.current_word_index + 1,
                                          'current_word' : GAME.actor.current_word,
                                          'incorrect' : incorrect,
                                          'outbound_url' : outbound_url})

def select_phrase(request):
    """
    The view for the select.html page.
    Gets random phrases from the phrases module using
    get_phrases_from_type
    """
    if GAME.actor is None:
        return redirect('/?no_actor=True')
    new_phrase_msg = ''
    if 'new_phrase' in request.GET:
        new_phrase_msg = new_phrase()
        #GAME.actor.phrase_complete() # reset current_phrase ect.
    return render(request, 'select_phrase.html', {'phrases' : get_phrases_from_type(5, 'ANY'),
                                                  'new_phrase' : new_phrase_msg})

def acting(request):
    """
    The default page for the actor while acting out a word/phrase
    """
    if GAME.actor is None:
        return redirect('/?no_actor=True')
    words_changable = False
    instructions_str = 'Act the Word!'
    if 'new_phrase' in request.GET:
        GAME.reset_guess_state() #reset current_correct_guess ect.
        words_changable = True
    phrase = GAME.actor.current_phrase
    ### Select phrase
    if 'phrase' in request.GET:
        phrase = request.GET['phrase']
        words_changable = True
        if "+" in phrase:
            phrase = phrase.replace("+", " ")
            instructions_str = select_word()
        if " " in phrase:
            instructions_str = select_word()
        genre = check_phrase(phrase)
        if genre is not None:
            GAME.actor.set_phrase(phrase, genre)
        else:
            raise RuntimeError("Phrase was not recognised as valid.")

    ### Select current word
    current_word_index = GAME.actor.current_word_index
    if 'current_word_index' in request.GET:
        GAME.reset_guess_state()
        current_word_index = request.GET['current_word_index']
        try:
            current_word_index = int(current_word_index)
        except RuntimeError:
            raise RuntimeError("Provided integer for current_word_index was not a number")
        if current_word_index < 1 or current_word_index > len(phrase.split()):
            raise RuntimeError("Provided word index %d is not in the range of the word" \
                               " with length %d." % (current_word_index, len(phrase.split)))
        else:
            GAME.actor.set_word(current_word_index - 1)

    ### Word polling response
    if 'word_complete' in request.GET:
        instructions_str = new_word()
        words_changable = True

    ### Render page
    return render(request,
                  'acting.html',
                  {'num_words' : len(GAME.actor.current_phrase_word_list),
                   'word_list' : GAME.actor.current_phrase_word_list,
                   'completed_words' : GAME.actor.completed_words,
                   'instructions' : instructions_str,
                   'current_word' : current_word_index,
                   'words_changable' : words_changable})


def waiting_for_actor(request):
    """
    Controller for waiting_for_actor.html
    Unique for each viewer
    """
    viewer_number = request.session['viewer_number']
    person = 'Someone else'
    if GAME.winning_viewer_number == viewer_number:
        person = 'You'
    viewer = GAME.lookup_viewer(viewer_number)
    position = GAME.get_viewer_position(viewer_number)
    points = viewer.points
    next_selection = 'Phrase'
    if GAME.current_correct_guess_type == 'Word' and \
       len(GAME.actor.completed_words) < len(GAME.actor.current_phrase_word_list):
        next_selection = 'Word'
    return render(request, 'waiting_for_actor.html',
                  {'person' : person,
                   'guess_type' : GAME.current_correct_guess_type,
                   'guess' : GAME.current_correct_guess,
                   'position' : position,
                   'points' : points,
                   'next_selection' : next_selection})


def reset(request):
    """
    resets the state of the game
    """
    global GAME
    GAME = Game()
    if 'user_type' in request.session:
        del request.session['user_type']
    if 'viewer_number' in request.session:
        del request.session['viewer_number']
    return redirect('/')


### ============================ API =================================== ###
def phrase_ready_api(request):
    """
    Asserts if the phrase is ready. Only intended for api access
    """
    phrase_ready = False
    if GAME is not None:
        if GAME.actor is not None:
            phrase_ready = GAME.actor.phrase_ready()
    return render(request, 'phrase_ready.html', {'phrase_ready' : phrase_ready})

def guess_correct_api(request):
    """
    None  :: Phrase has not been succesfully guessed / not ready to be guessed.
    Phrase :: The current Phrase has been correctly guessed.
    Word   :: The current word has been guessed correectly
    """
    guess_type = None
    if GAME is not None:
        guess_type = GAME.current_correct_guess_type
    return render(request, 'guess_correct.html', {'guess_type' : guess_type})
