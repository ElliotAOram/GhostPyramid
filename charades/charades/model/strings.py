"""Contains the editable strings for the Website"""

def actor_instructions():
    return "After you press continue, you will be given a choice of 5 different phrases." +\
           " Once you select a phrase by clicking it you will have a limited time act it out." +\
           " If the phrase is guess successfully you will be asked to choose a new phrase." +\
           " The more phrases that are guessed correctly, the more points you score."

def viewer_instructions():
    return "After the Actor has selected a phrase, you will have a limited time to guess it." +\
           " Look at the hologram in front of you to see what the actor is doing." +\
           " The faster you guess the phrase the more points you get." +\
           " You will be given some information about the current word or phrase to help you guess."

def actor_none():
    return "Requested page could not be loaded as no actor is present." +\
           " Please ensure an Actor has signed in using the correct session key."

def actor_already_defined():
    return "There is already an actor for that session ID. Please log in as a" +\
           " Viewer to participate."

def invalid_session():
    return "Invalid session ID has been provided."

def new_phrase():
    return "The Viewers have guessed your phrase! Please select a new phrase from the list below."

def new_word():
    return "The Viewers have guessed your word! Please select a new word using the buttons below."

def incorrect_guess():
    return "Incorrect! Try again!"

def select_word():
    return "Select a word using the buttons below and then start to Act it out!"

def invalid_state():
    return "That page can not be reached at this point in time. Please try again."

def incorrect_user():
    return "You do not have permission to access that page."

def not_accessible():
    return "That page is currently not accessible." 
