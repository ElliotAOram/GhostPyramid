"""Contains the VideoProcessor class (core application)"""
from copy import deepcopy
from cv2 import VideoCapture

def copy_video_feed(video):
    """
    Creats a deep copy of a VideoCapture object and returns it
    @param video    :: The VideoCapture object to be deepcopied
    @return the deepcopy of the VideoCapture
    @Raises ValueError  :: Raises ValueError on non VideoCapture input
    """
    if not isinstance(video, type(VideoCapture())):
        raise ValueError('Parameter is not a video')
    else:
        return deepcopy(video)


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


    def populate_video_feed_array(self, video):
        """
        Adds the video to the video_feed_array until there are four copies present
        @param video        :: The video to add to the array
        @Raises ValueError  :: Raises ValueError on non VideoCapture input
        """
        if  not isinstance(video, type(VideoCapture())):
            raise ValueError('Parameter is not a video')
        else:
            if self.video_feed_array is None:
                self.video_feed_array = []
            for _ in range(0, 4):
                self.video_feed_array.append(copy_video_feed(video))

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
