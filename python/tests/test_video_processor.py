"""Testing module for VideoProcessor class"""
import unittest

import cv2
import numpy as np

from .context import vpa
from random import randint

class TestInitForVidoeProcessor(unittest.TestCase):
    """
    @class TestInitVideoProcessor   :: Test the init functionality of the
                                       VideoProcessor class
    """
    ###--------------------------------Success cases-----------------------------------###
    def test_no_width_height_input(self):
        video_processor = vpa.VideoProcessor(background_colour = (0, 0, 0))
        self.assertIsInstance(video_processor.screen_width, int)
        self.assertIsInstance(video_processor.screen_height, int)
        self.assertEqual(video_processor.background_colour, (0, 0, 0))
        self.assertEqual(video_processor.threshold, 5)

    def test_width_input(self):
        video_processor = vpa.VideoProcessor(screen_width=1000,
                                             background_colour=(0, 0, 0))
        self.assertIsInstance(video_processor.screen_height, int)
        self.assertEqual(video_processor.screen_width, 1000)

    def test_height_input(self):
        video_processor = vpa.VideoProcessor(screen_height=1000,
                                             background_colour=(0, 0, 0))
        self.assertEqual(video_processor.screen_height, 1000)
        self.assertIsInstance(video_processor.screen_width, int)

    def test_threshold_input(self):
        video_processor = vpa.VideoProcessor(background_colour=(0, 0, 0),
                                             threshold=10)
        self.assertEqual(video_processor.threshold, 10)

    def test_non_zero_back_colour(self):
        video_processor = vpa.VideoProcessor(background_colour=(200, 100, 50))
        self.assertEqual(video_processor.background_colour[0], 200)
        self.assertEqual(video_processor.background_colour[1], 100)
        self.assertEqual(video_processor.background_colour[2], 50)

class TestCameraCapture(unittest.TestCase):
    """
    @Class TestCameraCapture    :: Tests the camera capture functionality of the
                                   VideoProcessor module.
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        self.video_processor = vpa.VideoProcessor((0,0,0))

    def tearDown(self):
        self.video_processor = None

    ###---------------------------------Success cases----------------------------------###
    def test_video_feed_initial_state(self):
        self.assertIsNone(self.video_processor.get_video_feed())

    def test_begin_capture_from_webcam(self):
        self.video_processor.begin_capture(0) # Starts capture with zeroth device (webcam)
        video_feed = self.video_processor.get_video_feed()
        self.assertIsNotNone(video_feed)
        self.assertIsInstance(video_feed, type(cv2.VideoCapture()))

    def test_end_capture_from_webcam(self):
        self.video_processor.begin_capture(0)
        self.video_processor.end_capture()
        self.assertIsNone(self.video_processor.get_video_feed())

    ###---------------------------------Failure cases---------------------------------###
    def test_begin_capture_with_non_int(self):
        self.assertRaises(ValueError,
                          self.video_processor.begin_capture,
                          'Not an int')

class TestScaleVideoFeed(unittest.TestCase):
    """
    @class TestVideoScaling     :: Tests that the video feed can be scaled based
                                   on a given resolution
    """
    ###================================setUp and tearDown=============================###
    def setUp(self):
        self.video_processor = vpa.VideoProcessor((0,0,0))
        self.video_processor.begin_capture(0)

    def tearDown(self):
        self.video_processor.end_capture()
        self.video_processor = None

    ###================================Success cases==================================###
    def test_up_scale_resolution(self):
        self.video_processor.scale_video_feed((1920, 1080))
        video_feed = self.video_processor.get_video_feed()
        new_scale_width = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        new_scale_height = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        self.assertEqual((1920, 1080), (new_scale_width, new_scale_height))

    def test_close_to_resolution(self):
        self.video_processor.scale_video_feed((1800, 900))
        video_feed = self.video_processor.get_video_feed()
        new_scale_width = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        new_scale_height = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        self.assertEqual((1920, 1080), (new_scale_width, new_scale_height))

    def test_same_resolution_as_video(self):
        self.video_processor.scale_video_feed((640, 480))
        video_feed = self.video_processor.get_video_feed()
        new_scale_width = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        new_scale_height = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        self.assertEqual((640, 480), (new_scale_width, new_scale_height))

    def test_scale_down_resolution(self):
        self.video_processor.scale_video_feed((320, 180))
        video_feed = self.video_processor.get_video_feed()
        new_scale_width = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        new_scale_height = video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        self.assertEqual((320, 180), (new_scale_width, new_scale_height))





###---------------------------frame creation functions----------------------------###
def create_simple_frame():
    simple_frame = np.zeros((200, 200, 3), dtype="uint8")
    simple_frame[0:200, 0:200] = [0, 0, 255]        # Red background
    simple_frame[90:110, 90:110] = [255, 0, 0]      # Blue foreground
    return simple_frame

def create_multichannel_frame():
    multi_frame = np.zeros((200, 200, 3), dtype="uint8")
    multi_frame[0:200, 0:200] = [0, 100, 150]           # Background
    multi_frame[90:110, 90:100] = [255, 100, 0]         # Foreground
    return multi_frame

def create_variation_frame(threshold):
    variation_frame = np.zeros((200, 200, 3), dtype="uint8")
    variation_frame[0:200, 0:200]                           # Background
    for frame in variation_frame:
        varaition = randint(0, threshold)
        frame = (0 + variation, 0 + variation, 255 - variation)
    variation_frame[90:110, 90:100] = [255, 0, 0]         # Foreground
    return viaration_frame


class TestBackgroundSubtraction(unittest.TestCase):
    """
    Test the background subtraction functionality
    """

    ###---------------------------------Success cases----------------------------------###
    def test_return_image(self):
        simple_frame = create_simple_frame()
        video_processor = vpa.VideoProcessor((0, 0, 0))
        subtracted_frame = video_processor.background_subtraction(simple_frame)
        self.assertIsInstance(subtracted_frame, type(np.array()))

    def test_no_channel_cross_and_no_variation(self):
        simple_frame = create_simple_frame()
        video_processor = vpa.VideoProcessor((0, 0, 255))
        subtracted_frame = video_processorbackground_subtraction(simple_frame)
        # Assert expected color for foreground picture
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][0], 255)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][1], 0)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][2], 0)
        # Assert colour for background pixel
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][0], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][1], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][2], 0)

    def test_channel_cross_and_no_variation(self):
        multi_frame = create_multichannel_frame()
        video_processor = vpa.VideoProcessor((0, 100, 150))
        subtracted_frame = video_processorbackground_subtraction(multi_frame)
        # Assert expected color for foreground picture
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][0], 255)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][1], 100)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][2], 0)
        # Assert colour for background pixel
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][0], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][1], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][2], 0)

    def test_no_channel_cross_and_variation_5(self):
        variation_frame = create_variation_frame(5)
        video_processor = vpa.VideoProcessor((0, 0, 255), threshold=5)
        subtracted_frame = video_processorbackground_subtraction(multi_variation)
        # Assert expected color for foreground picture
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][0], 255)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][1], 0)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][2], 0)
        # Assert colour for background pixel
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][0], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][1], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][2], 0)

    def test_no_channel_cross_and_variation_10(self):
        variation_frame = create_variation_frame(10)
        video_processor = vpa.VideoProcessor((0, 0, 255), threshold=10)
        subtracted_frame = video_processorbackground_subtraction(multi_variation)
        # Assert expected color for foreground picture
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][0], 255)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][1], 0)
        self.assertEqual(subtracted_frame[100:101, 100:101][0][0][2], 0)
        # Assert colour for background pixel
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][0], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][1], 0)
        self.assertEqual(subtracted_frame[2:3, 2:3][0][0][2], 0)
