"""Testing module for helper functions"""
import unittest

from .context import vpa

class TestScreenBoundaries(unittest.TestCase):
    """
    @class TestScreenBoundaries     :: Test the function that provides the maximum
                                       screen boundaries for the display
    """
    ###---------------------------------Success cases----------------------------------###
    def test_width_mt_height(self):
        """
        Tests that the correct square is calculate for supplied values were width
        is more than height.
        """
        coordinates = vpa.calculate_screen_boundaries(1000, 500)
        self.assertEqual((250,0)    , coordinates[0])
        self.assertEqual((750,500)  , coordinates[1])

    def test_height_mt_width(self):
        """
        Tests that the correct square is calculate for supplied values were height
        is more than width.
        """
        coordinates = vpa.calculate_screen_boundaries(500,1000)
        self.assertEqual((0,250)    , coordinates[0])
        self.assertEqual((500,750)  , coordinates[1])

    def test_output_with_no_params(self):
        """
        Test that nothing fails when the no parameters are supplied. The actually values
        can't be tested here as it will dependant on the machnine that it is run on, but
        type and format can be checked.
        """
        coordinates = vpa.calculate_screen_boundaries()
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
                          vpa.calculate_screen_boundaries,
                          "not int",
                          "not int")

        self.assertRaises(ValueError,
                          vpa.calculate_screen_boundaries,
                          0,
                          100)

        self.assertRaises(ValueError,
                          vpa.calculate_screen_boundaries,
                          100,
                          -1)


class TestCalculateImagePositions(unittest.TestCase):
    """
    @class TestCalculateImagePositions      :: Test the function that positions the image
                                               in the correct area of the frame
    """

    ###---------------------------------Success cases----------------------------------###
    def test_square_image_size(self):
        """
        Test that a square image is placed correctly.
        This test will check the boundaries of the image.
        """
        coord_map = vpa.calculate_image_positions(500, 100, 100)
        self.assertEqual([200,0  ]  , coord_map["top"][0])
        self.assertEqual([300,100]  , coord_map["top"][1])
        self.assertEqual([0,200  ]  , coord_map["left"][0])
        self.assertEqual([100,300]  , coord_map["left"][1])
        self.assertEqual([200,400]  , coord_map["bottom"][0])
        self.assertEqual([300,500]  , coord_map["bottom"][1])
        self.assertEqual([400,200]  , coord_map["right"][0])
        self.assertEqual([500,300]  , coord_map["right"][1])

    def test_long_width_image_size(self):
        """
        Test that a longer width image is placed correctly.
        This test will check the boundaries of the image.
        """
        coord_map = vpa.calculate_image_positions(500, 100, 50)
        self.assertEqual([200,0  ]  , coord_map["top"][0])
        self.assertEqual([300,50 ]  , coord_map["top"][1])
        self.assertEqual([0,225  ]  , coord_map["left"][0])
        self.assertEqual([100,275]  , coord_map["left"][1])
        self.assertEqual([200,450]  , coord_map["bottom"][0])
        self.assertEqual([300,500]  , coord_map["bottom"][1])
        self.assertEqual([400,225]  , coord_map["right"][0])
        self.assertEqual([500,275]  , coord_map["right"][1])

    def test_long_height_image_size(self):
        """
        Test that a longer height image is placed correctly.
        This test will check the boundaries of the image.
        """
        coord_map = vpa.calculate_image_positions(500, 50, 100)
        self.assertEqual([225,0  ]  , coord_map["top"][0])
        self.assertEqual([275,100]  , coord_map["top"][1])
        self.assertEqual([0,200  ]  , coord_map["left"][0])
        self.assertEqual([50,300 ]  , coord_map["left"][1])
        self.assertEqual([225,400]  , coord_map["bottom"][0])
        self.assertEqual([275,500]  , coord_map["bottom"][1])
        self.assertEqual([450,200]  , coord_map["right"][0])
        self.assertEqual([500,300]  , coord_map["right"][1])


    ###---------------------------------Failure cases----------------------------------###
    def test_non_int_zero_negative_input(self):
        """
        Ensure function raises a ValueError if screenlength is non int
        """
        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          "not int", 1, 1)

        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          1, 0, 1)

        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          1, 1, -1)


class TestGetScreenDimensions(unittest.TestCase):
    """
    Ensures that the get_screen_width_and_height functions correctly
    """

    def test_correct_type_and_format(self):
        screen_dimension = vpa.get_screen_width_and_height()
        self.assertIsInstance(screen_dimension[0], int)
        self.assertIsInstance(screen_dimension[1], int)


class TestCreateImagePositionDictionary(unittest.TestCase):
    """
    Test the workflow function that strings together the above
    functions for use in the output_video function
    """
    ###---------------------------------Success cases----------------------------------###
    def test_create_normal_dictionary(self):
        img_pos = vpa.create_image_position_dictionary(200, 100, 10, 10)
        self.assertEqual([95,0   ]  , img_pos["top"][0])
        self.assertEqual([105,10 ]  , img_pos["top"][1])
        self.assertEqual([50,45  ]  , img_pos["left"][0])
        self.assertEqual([60,55  ]  , img_pos["left"][1])
        self.assertEqual([95,90  ]  , img_pos["bottom"][0])
        self.assertEqual([105,100]  , img_pos["bottom"][1])
        self.assertEqual([140,45  ]  , img_pos["right"][0])
        self.assertEqual([150,55 ]  , img_pos["right"][1])

    ###---------------------------------Failure cases-----------------------------------###
    def test_raises_valueError_on_non_int_or_zero(self):
        self.assertRaises(ValueError,
                          vpa.create_image_position_dictionary,
                          "not int", 1, 1, 1)

        self.assertRaises(ValueError,
                          vpa.create_image_position_dictionary,
                          1, 0, 1, 1)

        self.assertRaises(ValueError,
                          vpa.create_image_position_dictionary,
                          1, 1, -1, 1)



##Input parser function tests



class TestPositiveParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """
    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(vpa.parse_positive_int(0))

    def test_positive(self):
        self.assertTrue(vpa.parse_positive_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_negative(self):
        self.assertRaises(ValueError,
                          vpa.parse_positive_int,
                          -1)

class TestNonZeroParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      non zero integers
    """

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(vpa.parse_non_zero_int(-10))

    def test_positive(self):
        self.assertTrue(vpa.parse_non_zero_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_zero(self):
        self.assertRaises(ValueError,
                          vpa.parse_non_zero_int,
                          0)

class TestIntParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(vpa.parse_int(0))


    ###---------------------------------Failure cases-----------------------------------###

    def test_raise_ValueError_on_non_int(self):
        self.assertRaises(ValueError,
                          vpa.parse_int,
                          "Non int")
