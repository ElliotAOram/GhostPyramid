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
            False
