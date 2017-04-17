"""
Module for the Viewer class
"""

class Viewer(object):
    """
    The class for the user of type Viewer
    """

    name = 'anonymous'
    points = 0
    viewer_number = None

    def __init__(self, viewer_num):
        self.name = 'anonymous'
        self.points = 0
        self.viewer_number = viewer_num

    def increment_points(self, points_to_add):
        self.points += int(points_to_add)

    def set_name(self, new_name):
        self.name = str(new_name)
