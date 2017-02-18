import numpy as np
import cv2

class VideoProcessor:

	# Global variable for video feed
	video_feed = None

	'''
	Begins capturing video from an external device and updates
	the video_feed object with the camera output.

	@param device		:: The integer that corresponds to the device
	@Raises ValueError 	:: Raises ValueError on non integer input
	'''
	def begin_capture(self, device):
		try:
			integer = int(device)
		except ValueError:
			raise ValueError('Value provided is not an integer')

		self.video_feed = cv2.VideoCapture(device)

	'''
	Ends capturing video from the current video_feed. Sets the video_feed
	object make to None to avoid misuse
	'''
	def end_capture(self):
		self.video_feed.release()
		self.video_feed = None

	'''
	Returns the video_feed currently in use
	@return video_feed		:: The current video feed from a camera
	'''
	def get_video_feed(self):
		return self.video_feed
