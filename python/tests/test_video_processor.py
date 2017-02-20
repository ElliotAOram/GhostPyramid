"""Testing module for VideoProcessor class"""
import unittest

from cv2 import VideoCapture
from .context import vpa


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

    ###---------------------------------Failure cases---------------------------------###
    def test_begin_capture_with_non_int(self):
        """
        vpa.begin_capture only supports integer input.
        If a non-integer is provided, then an exception is raised.
        """
        self.assertRaises(ValueError,
                          self.video_processor.begin_capture,
                          'Not an int')

if __name__ == '__main__':
    unittest.main()
