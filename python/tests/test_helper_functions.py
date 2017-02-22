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
        coordinates = calculate_screen_boundaries(1000, 500)
        self.assertEqual((250,0), coordinates[0])
        self.assertEqual((750,500), coordinates[1])
        
        
    def test_height_mt_width(self):
        """
        Tests that the correct square is calculate for supplied values were height
        is more than width.
        """
        coordinates = calculate_screen_boundaries(500,1000)
        self.assertEqual((0,250), coordinates[0])
        self.assertEqual((500,750), coordinates[1])
        

    def test_output_with_no_params(self):
        """
        Test that nothing fails when the no parameters are supplied. The actually values
        can't be tested here as it will dependant on the machnine that it is run on, but
        type and format can be checked.
        """
        coordinates = calculate_screen_boundaries()
        self.assertIsInstance(coordinates[0][0], int)
        self.assertIsInstance(coordinates[0][1], int)
        self.assertIsInstance(coordinates[1][0], int)
        self.assertIsInstance(coordinates[1][1], int)

    ###---------------------------------Failure cases----------------------------------###

    def test_raise_ValueError_with_non_int(self):
        """
        Ensures that the function produces a value error if integers are not supplied
        """
        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          "not int",
                          "not int")
    
    def test_raise_ValueError_with_0_width(self):
        """
        Ensures that the function produces a ValueError if a zero is provided
        """
        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          0,
                          100)

    def test_raise_ValueError_with_0_height(self):
        """
        Ensures that the function produces a ValueError if a zero is provided
        """
        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          100,
                          0)


class TestCalculateImagePositions(unittest.TestCase):
    """
    @class TestCalculateImagePositions      :: Test the function that positions the image
                                               in the correct area of the frame
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    ###---------------------------------Success cases----------------------------------###
    def test_normal_image_size(self):
        """
        Test that a normal size image is placed correctly.
        This test will check the boundaries of the image.
        """
        

    ###---------------------------------Failure cases----------------------------------###
    def test_non_int_screen_length(self):
        """
        Ensure function raises a ValueError if screenlength is non int
        """
        

    def test_non_int_width(self):
        """
        Ensure function raises a ValeError is width is non int
        """
    

    def test_non_int_height(self):
        """
        Ensure function raises a ValueError is height is non int
        """
    
