"""
Module for the Viewer class
"""
#pylint: disable=too-few-public-methods
class Viewer(object):
    """
    The class for the user of type Viewer
    """

    points = 0
    viewer_number = None

    def __init__(self, viewer_num):
        self.points = 0
        self.viewer_number = viewer_num

    def increment_points(self, points_to_add):
        self.points += int(points_to_add)
