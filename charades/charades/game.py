"""
Module for the Game class
"""
from viewer import Viewer

class Game(object):
    """
    The class that holds a game instance
    """

    actor = None
    viewers = []
    current_correct_guess = None
    current_correct_guess_type = None
    winning_viewer_number = None

    def __init__(self):
        self.actor = None
        self.viewers = []
        self.current_correct_guess = None
        self.current_correct_guess_type = None
        self.winning_viewer_number = None

    def add_actor(self, actor):
        """
        Adds an actor providing actor is None.
        @param actor    :: The new actor to add
        @return bool for if variable was added successfully
        """
        if self.actor is None:
            self.actor = actor
            return True
        else:
            return False

    def add_viewer(self):
        """
        Adds a viewer providing there are less viewers than the maximum
        @return the current viewer number or false.
        """
        if len(self.viewers) <= 5:
            viewer_num = len(self.viewers) + 1
            self.viewers.append(Viewer(viewer_num))
            return viewer_num
        else:
            return False

    def lookup_viewer(self, viewer_num):
        """
        Look up the viewer by viewer_number
        @param viewer_num   :: The viewer_number to look for
        @return viewer or False
        @raises RuntimeError :: If the multiple viewers are
                                found with the same id
        """
        viewer = [viewer for viewer in self.viewers
                  if viewer.viewer_number == viewer_num]
        if len(viewer) == 1:
            return viewer[0]
        elif len(viewer) > 1:
            # This should not be possible due to the implementation but is checked
            # for clarity
            raise RuntimeError('Viewer lookup returned a list not a single viewer')
        else:
            return []

    def get_viewer_position(self, viewer_num):
        """
        Looks up the viewers score and their position relative to other viewers
        @param viewer_num  :: The viewer number to lookup the position of
        @return The position as a string
        """
        current_viewer_points = self.lookup_viewer(viewer_num).points
        position = 1
        for viewer in self.viewers:
            if viewer.points > current_viewer_points:
                position += 1
        def position_string(number):
            return {
                1: '1st',
                2: '2nd',
                3: '3rd',
            }[number]
        if position <= 3:
            return position_string(position)
        else:
            return str(position) + 'th'

    def set_guess_type(self, is_phrase):
        """
        Takes a boolean to represent if the guess type is for the phrase (True)
        or the word (False)
        @param is_phrase    :: True/False
        """
        if isinstance(is_phrase, bool):
            if is_phrase is True:
                self.current_correct_guess_type = 'Phrase'
            else:
                self.current_correct_guess_type = 'Word'
        else:
            return False

    def set_guess(self, guess):
        """
        Sets the current correct guess and verify that the guess is correct
        Function will assume a guess type if not already set (is None)
        """
        # If no guess type set (should not be the case) then the guess type is
        # assumed by a space in the guess
        if self.current_correct_guess_type is None:
            if ' ' in guess:
                self.current_correct_guess_type = 'Phrase'
            else:
                self.current_correct_guess_type = 'Word'

        if self.current_correct_guess_type == 'Word':
            if self.actor.current_word.upper() == guess.upper():
                # use actor version of word to account for capitalisation
                self.current_correct_guess = self.actor.current_word
            else:
                return False
        else: # guess type is Phrase
            if self.actor.current_phrase.upper() == guess.upper():
                # use actor version of word to account for capitalisation
                self.current_correct_guess = self.actor.current_phrase
            else:
                return False

    def reset_guess_state(self):
        """
        Resets correct guess states to None
        """
        self.current_correct_guess = None
        self.current_correct_guess_type = None
