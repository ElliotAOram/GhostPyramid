"""Contains the VideoProcessor class (core application)"""
import cv2
from helper_functions import *
import numpy as np


class VideoProcessor(object):
    """
    @class VideoProcessor   :: Handles the flow of the project from video
                               input capture to video output.
    """

    def __init__(self):
        self.video_feed = None


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

        self.video_feed = cv2.VideoCapture(device)


    def end_capture(self):
        """
        Ends capturing video from the current video_feed.
        Sets the video_feed object make to None to avoid misuse.
        """
        self.video_feed.release()
        self.video_feed = None


    def output_video(self):
        """
        Outputs all video_feeds to a single output window
        """
        #Establish image and monitor dimensions
        screen_res = get_screen_width_and_height()
        frame_width = int(self.video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.video_feed.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

        # Feed into functions to calculate display area and image positions
        display_area = calculate_screen_boundaries(screen_res[0], screen_res[1])
        display_side_length = abs(display_area[1][1] - display_area[0][1])
        displacement = max(display_area[0][0], display_area[0][1])

        img_positions = calculate_image_positions(display_side_length,
                                                  frame_width, frame_height)

        # Apply displacement
        for _, value in img_positions.iteritems():
            value[0][0] += displacement
            value[1][0] += displacement

        while (True):
            _, frame = self.video_feed.read()
            #http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
            merged_frame = np.zeros((screen_res[1], screen_res[0], 3), dtype="uint8")
            merged_frame[img_positions["top"][0][1]:img_positions["top"][1][1],
                         img_positions["top"][0][0]:img_positions["top"][1][0]] = frame

            merged_frame[img_positions["left"][0][1]:img_positions["left"][1][1],
                         img_positions["left"][0][0]:img_positions["left"][1][0]] = frame

            merged_frame[img_positions["bottom"][0][1]:img_positions["bottom"][1][1],
                         img_positions["bottom"][0][0]:img_positions["bottom"][1][0]] = frame

            merged_frame[img_positions["right"][0][1]:img_positions["right"][1][1],
                         img_positions["right"][0][0]:img_positions["right"][1][0]] = frame

            #http://stackoverflow.com/questions/17696061/how-to-display-a-full-screen-images-with-python2-7-and-opencv2-4
            cv2.namedWindow("Output Window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Output Window", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            cv2.imshow("Output Window", merged_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.end_capture()
        cv2.destroyAllWindows()

    def get_video_feed(self):
        """
        Returns the video_feed currently in use.
        @return video_feed      :: The current video feed from a camera.
        """
        return self.video_feed
