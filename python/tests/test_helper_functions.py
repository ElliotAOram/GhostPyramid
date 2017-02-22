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
        self.assertEqual((250,0)    , coordinates[0])
        self.assertEqual((750,500)  , coordinates[1])

    def test_height_mt_width(self):
        """
        Tests that the correct square is calculate for supplied values were height
        is more than width.
        """
        coordinates = calculate_screen_boundaries(500,1000)
        self.assertEqual((0,250)    , coordinates[0])
        self.assertEqual((500,750)  , coordinates[1])

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

    def test_non_int_zero_negative_input(self):
        """
        Ensures that the function produces a value error if integers are not supplied
        """
        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          "not int",
                          "not int")

        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          0,
                          100)

        self.assertRaises(ValueError,
                          calculate_screen_boundaries,
                          100,
                          -1)


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
        coord_map = calculate_image_positions(500, 100, 100)
        self.assertEqual((200,0)    , coord_map["top"][0])
        self.assertEqual((300,100)  , coord_map["top"][1])
        self.assertEqual((0,200)    , coord_map["left"][0])
        self.assertEqual((100,300)  , coord_map["left"][1])
        self.assertEqual((200,400)  , coord_map["bottom"][0])
        self.assertEqual((300,500)  , coord_map["bottom"][1])
        self.assertEqual((400,200)  , coord_map["right"][0])
        self.assertEqual((500,300)  , coord_map["right"][1])


    ###---------------------------------Failure cases----------------------------------###
    def test_non_int_zero_negative_input(self):
        """
        Ensure function raises a ValueError if screenlength is non int
        """
        self.assertRaises(ValueError,
                          calculate_image_positions,
                          "not int", 1, 1)

        self.assertRaises(ValueError,
                          calculate_image_positions,
                          1, 0, 1)

        self.assertRaises(ValueError,
                          calculate_image_positions,
                          1, 1, -1)




##Input parser function tests



class TestPositiveParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(parse_positive_int(0))

    def test_positive(self):
        self.assertTrue(parse_positive_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_negative(self):
        self.assertRaises(ValueError,
                          parse_positive_int,
                          -1)

class TestNonZeroParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      non zero integers
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(parse_non_zero_int(-10))

    def test_positive(self):
        self.assertTrue(parse_non_zero_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_zero(self):
        self.assertRaises(ValueError,
                          parse_non_zero_int,
                          0)

class TestIntParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(parse_int(0))


    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_non_int(self):
        self.assertRaises(ValueError,
                          parse_int,
                          "Non int")
