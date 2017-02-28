"""Testing module for helper functions"""
import unittest
import numpy as np

from .context import vpa

class TestGetScreenDimensions(unittest.TestCase):
    """
    Ensures that the get_screen_width_and_height functions correctly
    """

    def test_correct_type_and_format(self):
        screen_dimension = vpa.get_screen_resolution()
        self.assertIsInstance(screen_dimension[0], int)
        self.assertIsInstance(screen_dimension[1], int)


class TestScreenBoundaries(unittest.TestCase):
    """
    @class TestScreenBoundaries     :: Test the function that provides the maximum
                                       screen boundaries for the display
    """
    ###---------------------------------Success cases----------------------------------###
    def test_width_mt_height(self):
        side, displacement = vpa.calculate_display_area_properties(1000, 500)
        self.assertEqual(500, side)
        self.assertEqual(250, displacement)

    def test_height_mt_width(self):
        side, displacement = vpa.calculate_display_area_properties(500, 1000)
        self.assertEqual(500, side)
        self.assertEqual(250, displacement)

    ###---------------------------------Failure cases----------------------------------###

    def test_non_int_zero_negative(self):
        self.assertRaises(ValueError,
                          vpa.calculate_display_area_properties,
                          "not int",
                          "not int")

        self.assertRaises(ValueError,
                          vpa.calculate_display_area_properties,
                          0, 100)

        self.assertRaises(ValueError,
                          vpa.calculate_display_area_properties,
                          100, -1)


class TestCalculateImagePositions(unittest.TestCase):
    """
    @class TestCalculateImagePositions      :: Test the function that positions the image
                                               in the correct area of the frame
    """

    ###---------------------------------Success cases----------------------------------###
    def test_square_image_size(self):
        coord_map = vpa.calculate_image_positions(500, 100, 100)
        self.assertEqual([200, 0], coord_map["top"][0])
        self.assertEqual([300, 100], coord_map["top"][1])
        self.assertEqual([0, 200], coord_map["left"][0])
        self.assertEqual([100, 300], coord_map["left"][1])
        self.assertEqual([200, 400], coord_map["bottom"][0])
        self.assertEqual([300, 500], coord_map["bottom"][1])
        self.assertEqual([400, 200], coord_map["right"][0])
        self.assertEqual([500, 300], coord_map["right"][1])

    def test_long_width_image_size(self):
        coord_map = vpa.calculate_image_positions(500, 100, 50)
        self.assertEqual([200, 0], coord_map["top"][0])
        self.assertEqual([300, 50], coord_map["top"][1])
        self.assertEqual([0, 225], coord_map["left"][0])
        self.assertEqual([100, 275], coord_map["left"][1])
        self.assertEqual([200, 450], coord_map["bottom"][0])
        self.assertEqual([300, 500], coord_map["bottom"][1])
        self.assertEqual([400, 225], coord_map["right"][0])
        self.assertEqual([500, 275], coord_map["right"][1])

    def test_long_height_image_size(self):
        coord_map = vpa.calculate_image_positions(500, 50, 100)
        self.assertEqual([225, 0], coord_map["top"][0])
        self.assertEqual([275, 100], coord_map["top"][1])
        self.assertEqual([0, 200], coord_map["left"][0])
        self.assertEqual([50, 300], coord_map["left"][1])
        self.assertEqual([225, 400], coord_map["bottom"][0])
        self.assertEqual([275, 500], coord_map["bottom"][1])
        self.assertEqual([450, 200], coord_map["right"][0])
        self.assertEqual([500, 300], coord_map["right"][1])


    ###---------------------------------Failure cases----------------------------------###
    def test_non_int_zero_negative(self):
        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          "not int", 1, 1)

        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          1, 0, 1)

        self.assertRaises(ValueError,
                          vpa.calculate_image_positions,
                          1, 1, -1)


class TestGetIdealImageResolution(unittest.TestCase):
    """
    Test the workflow function that strings together the above
    functions for use in the output_video function
    """
    ###---------------------------------Success cases----------------------------------###
    def test_1080_display_length(self):
        resolution = vpa.get_ideal_image_resolution(1080)
        self.assertEqual(resolution, (640, 480))

    def test_larger_than_known(self):
        resolution = vpa.get_ideal_image_resolution(999999)
        # Should return largest known display scale
        self.assertEqual(resolution, (1920, 1080))

    def test_small_display_area(self):
        resolution = vpa.get_ideal_image_resolution(200)
        self.assertEqual(resolution, (320, 180))

    ###---------------------------------Failure cases-----------------------------------###
    def test_input_non_int_or_zero(self):
        self.assertRaises(ValueError,
                          vpa.get_ideal_image_resolution,
                          "not int")

        self.assertRaises(ValueError,
                          vpa.get_ideal_image_resolution,
                          0)

        self.assertRaises(ValueError,
                          vpa.get_ideal_image_resolution,
                          -1)

class TestCalculateCropRange(unittest.TestCase):
    """
    Test that the crop range is correctly calculated and returned in the expected form
    """
    ###---------------------------------Success cases----------------------------------###
    def test_valid_crop_range(self):
        crop_range = vpa.calculate_crop_range((640, 480), 360)

    def test_max_img_size_mt_res(self):
        crop_range = vpa.calculate_crop_range((500,500), 600)
        


    ###---------------------------------Failure cases-----------------------------------###
    def test_non_int_input(self):
        self.assertRaises(ValueError, 
                          vpa.calculate_crop_range,
                          ("not int","not int"), "not int")

    def test_positive_int(self):
        self.assertRaises(ValueError,
                          vpa.calculate_crop_range,
                          (-1,-1), -1)

    def test_non_zero_input(self):
        self.assertRaises(ValueError,
                          vpa.calculate_crop_range,
                          (0,0), 0)


class TestRotateImageClockwise(unittest.TestCase):
    """
    Test that an image is correctly rotated through a given angle
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        self.frame = np.zeros((200, 200, 3), dtype="uint8")
        self.frame[0:2, 0:2] = [255, 0, 0]

    def tearDown(self):
        self.frame = None
        

    ###---------------------------------Success cases----------------------------------###
    def test_no_rotation(self):
        rotated_frame = vpa.rotate_image_anticlockwise(self.frame, 200, 0)
        # Assert expected color for modified pixel
        self.assertEqual(self.frame[0:1, 0:1][0][0][0], 255)
        self.assertEqual(self.frame[0:1, 0:1][0][0][1], 0)
        self.assertEqual(self.frame[0:1, 0:1][0][0][2], 0)
        # Assert colour for non modified pixel
        self.assertEqual(self.frame[2:3, 2:3][0][0][0], 0)
        self.assertEqual(self.frame[2:3, 2:3][0][0][1], 0)
        self.assertEqual(self.frame[2:3, 2:3][0][0][2], 0)
        

    def test_90_degree_rotation(self):
        self.frame = vpa.rotate_image_anticlockwise(self.frame, 200, 90)
        # Assert expected color for modified pixel
        self.assertEqual(self.frame[199:200, 0:1][0][0][0], 255)
        self.assertEqual(self.frame[199:200, 0:1][0][0][1], 0)
        self.assertEqual(self.frame[199:200, 0:1][0][0][2], 0)
        # Assert colour for non modified pixel
        self.assertEqual(self.frame[198:199, 198:199][0][0][0], 0)
        self.assertEqual(self.frame[198:199, 198:199][0][0][1], 0)
        self.assertEqual(self.frame[198:199, 198:199][0][0][2], 0)
