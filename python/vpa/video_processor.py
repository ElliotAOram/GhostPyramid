"""Contains the VideoProcessor class (core application)"""
from cv2 import VideoCapture
from copy import deepcopy


class VideoProcessor(object):
    """
    @class VideoProcessor   :: Handles the flow of the project from video
                               input capture to video output.
    """

    def __init__(self):
        self.video_feed = None
        self.video_feed_array = None


    def begin_capture(self, device):
        """
        Begins capturing video from an external device and updates
        the video_feed object with the camera output.

        @param device		:: The integer that corresponds to the device.
        @Raises ValueError 	:: Raises ValueError on non integer input.
        """
        try:
            int(device)
        except ValueError:
            raise ValueError('Value provided is not an integer')

        self.video_feed = VideoCapture(device)


    def end_capture(self):
        """
        Ends capturing video from the current video_feed.
        Sets the video_feed object make to None to avoid misuse.
        """
        self.video_feed.release()
        self.video_feed = None

    def copy_video_feed(self, video):
        """
        Creats a deep copy of a VideoCapture object and returns it
        """
        return deepcopy(video)


    def get_video_feed(self):
        """
        Returns the video_feed currently in use.
        @return video_feed      :: The current video feed from a camera.
        """
        return self.video_feed

    def get_video_feed_array(self):
        """
        Returns the video_feed_array contianing all the processed video feeds.
        @return video_feed_array
        """
        return self.video_feed_array
