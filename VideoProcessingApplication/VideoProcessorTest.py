import unittest
from VideoProcessor import VideoProcessor

class testCameraCapture(unittest.TestCase):

	###------------------------------setUp and tearDown--------------------------------###
	def setUp(self):
		self.vp = VideoProcessor()

	def tearDown(self):
		self.widget = None

	###---------------------------------Success cases----------------------------------###
	def test_video_feed_is_initially_null(self):
		self.assertIsNone(self.vp.get_video_feed())

	def test_begin_capture_from_webcam(self):
		self.vp.begin_capture(0) # Starts capture with zeroth device (webcam)
		self.assertIsNotNone(self.vp.get_video_feed())

	def test_end_capture_from_webcam(self):
		self.vp.begin_capture(0)
		self.vp.end_capture()
		self.assertIsNone(self.vp.get_video_feed())

	###---------------------------------Failure cases---------------------------------###
	def test_non_int_value_to_begin_capture_function(self):
		self.assertRaises(ValueError, self.vp.begin_capture, 'Not an int')

if __name__ == '__main__':
    unittest.main()
