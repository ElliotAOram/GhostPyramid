"""Testing module for helper functions"""
import unittest

from .context import helperfunctions

class TestScreenBoundaries(unittest.TestCase):
    """
    @class TestScreenBoundaries     :: Test the function that provides the maximum 
                                       screen boundaries for the display
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    ###---------------------------------Success cases----------------------------------###
    def test_width_mt_height(self):
        """
        Tests that the correct square is calculate for supplied values were width
        is more than height.
        """

    def test_height_mt_width(self):
        """
        Tests that the correct square is calculate for supplied values were height
        is more than width.
        """

    def test_output_with_no_params(self):
        """
        Test that nothing fails when the no parameters are supplied. The actually values
        can't be tested here as it will dependant on the machnine that it is run on, but
        type and format can be checked.
        """


    ###---------------------------------Failure cases----------------------------------###

    def test_raise_ValueError_with_non_int(self):
        """
        Ensures that the function produces a value error if integers are not supplied
        """