"""
Module for the Game class
"""

class Game(object):
    """
    The class that holds a game instance
    """

    actor = None
    viewers = []

    def __init__(self):
        self.actor = None
        self.viewers = []

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

    def add_viewer(self, viewer):
        """
        Adds a viewer providing there are less viewers than the maximum
        @param viewer   :: The new viewer to add
        @return the current viewer number or false.
        """
        if len(self.viewers) <= 5:
            self.viewers.append(viewer)
            return len(self.viewers)
        else:
            return False
