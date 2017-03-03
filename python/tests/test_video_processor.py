"""Testing module for VideoProcessor class"""
import unittest

import cv2

from .context import vpa

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
        video_processor = vpa.VideoProcessor(background_colour(200, 100, 50))
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
        self.video_processor = vpa.VideoProcessor()

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
        self.video_processor = vpa.VideoProcessor()
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
