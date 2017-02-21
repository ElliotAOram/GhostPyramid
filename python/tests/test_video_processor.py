"""Testing module for VideoProcessor class"""
import unittest

from cv2 import VideoCapture
from .context import vpa


class TestCameraCapture(unittest.TestCase):
    """
    @class TestCameraCapture    :: Tests the camera capture functionality of the
                                   VideoProcessor module.
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        self.video_processor = vpa.VideoProcessor()

    def tearDown(self):
        self.video_processor = None

    ###---------------------------------Success cases----------------------------------###
    def test_video_feed_initial_state(self):
        """
        Initial state of video_feed variable should be None
        """
        self.assertIsNone(self.video_processor.get_video_feed())

    def test_begin_capture_from_webcam(self):
        """
        Ensure that when the video_feed is started, the object is no
        longer and is of type Video.
        """
        self.video_processor.begin_capture(0) # Starts capture with zeroth device (webcam)
        video_feed = self.video_processor.get_video_feed()
        self.assertIsNotNone(video_feed)
        self.assertIsInstance(video_feed, type(VideoCapture()))

    def test_end_capture_from_webcam(self):
        """
        Ensure that the camera is correctly released after use
        """
        self.video_processor.begin_capture(0)
        self.video_processor.end_capture()
        self.assertIsNone(self.video_processor.get_video_feed())

    ###---------------------------------Failure cases----------------------------------###
    def test_begin_capture_with_non_int(self):
        """
        vpa.begin_capture only supports integer input.
        If a non-integer is provided, then an exception is raised.
        """
        self.assertRaises(ValueError,
                          self.video_processor.begin_capture,
                          'Not an int')

class TestVideoFeedCoping(unittest.TestCase):
    """
    @class TestVideoFeedCoping      :: Tests the functionality for copying the video_feed
                                       and populating the video_feed_array
    """
    ###------------------------------setUp and tearDown--------------------------------###
    def setUp(self):
        self.video_processor = vpa.VideoProcessor()
        self.video_processor.begin_capture(0)

    def tearDown(self):
        self.video_processor.end_capture()
        self.video_processor = None

    ###---------------------------------Success cases----------------------------------###
    def test_initial_state_of_video_feed_array(self):
        """
        Tests that the video_feed_array is initialised to None
        """
        video_feed_array = self.video_processor.get_video_feed_array()
        self.assertIsNone(video_feed_array)

    def test_copy_video_feed(self):
        """
        Test that the video_feed is copied.
        Ensure the type is correct and the video_feed is a deep copy.
        """
        original_video = self.video_processor.get_video_feed()
        new_video = self.video_processor.copy_video_feed(original_video)
        self.assertEqual(type(original_video), type(new_video))

    def test_populate_video_feed_array(self):
        """
        Test that the video_feed_array is correctly populated
        after a call to the function
        """
        original_video = self.video_processor.get_video_feed()
        self.video_processor.populate_video_feed_array(original_video)
        video_feed_array = self.video_processor.get_video_feed_array()
        self.assertEqual(4, len(video_feed_array))
        for video_feed in video_feed_array:
            self.assertIsInstance(video_feed, type(VideoCapture()))

    ###---------------------------------Failure cases----------------------------------###
    def test_copy_video_feed_with_non_VideoCapture(self):
        """
        Test that only an object of type VideoCapture can be a parameter
        of copy_video_feed
        """
        self.assertRaises(ValueError,
                          self.video_processor.copy_video_feed,
                          "Not a video")

    def test_populate_video_feed_array_with_non_video(self):
        """
        Test that only an object of type VideoCapture can be a parameter
        of copy_video_feed
        """
        self.assertRaises(ValueError,
                          self.video_processor.populate_video_feed_array,
                          "Not a video")
