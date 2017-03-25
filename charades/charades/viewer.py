"""
Module for the Viewer class
"""

class Viewer(object):

    name = 'anonymous'
    points = 0

    def __init__(self):
        self.name = 'anonymous'
        self.points = 0

    def increment_points(self, points_to_add):
        self.points += int(points_to_add)

    def set_name(self, new_name):
        self.name = str(new_name)
