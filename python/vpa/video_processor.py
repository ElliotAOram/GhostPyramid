"""Contains the VideoProcessor class (core application)"""
import cv2
from helper_functions import get_screen_resolution, calc_display_area_props, \
                             get_ideal_image_resolution, calculate_image_positions, \
                             calculate_crop_range, rotate_image_anticlockwise
import numpy as np
import threading
from multiprocessing import Pool
from parsers import parse_positive_int


IDENTIFIERS = ["top", "left", "bottom", "right"]


class VideoProcessor(object):
    """
    @class VideoProcessor   :: Handles the flow of the project from video
                               input capture to video output.
    """

    def __init__(self, background_colour, screen_width=None,
                 screen_height=None, threshold=None):
        self.video_feed = None
        self.background_colour = background_colour

        if screen_width is None:
            self.screen_width = get_screen_resolution()[0]
        else:
            self.screen_width = screen_width

        if screen_height is None:
            self.screen_height = get_screen_resolution()[1]
        else:
            self.screen_height = screen_height

        if threshold is None:
            self.threshold = 5
        else:
            self.threshold = threshold


    def begin_capture(self, device):
        """
        Begins capturing video from an external device and updates
        the video_feed object with the camera output.

        @param device		:: The integer that corresponds to the device.
        @Raises ValueError 	:: Raises ValueError on non integer input.
        """
        parse_positive_int(device)
        self.video_feed = cv2.VideoCapture(device)


    def end_capture(self):
        """
        Ends capturing video from the current video_feed.
        Sets the video_feed object make to None to avoid misuse.
        """
        self.video_feed.release()
        self.video_feed = None


    def scale_video_feed(self, desired_resolution):
        """
        scales the video_feed to the desired resolution
        @param desired_resolution    :: The resolution desired for the video_feed
        """
        self.video_feed.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, desired_resolution[0])
        self.video_feed.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, desired_resolution[1])


    def process_and_output_video(self):
        """
        Outputs all video_feeds to a single output window
        """

        # Get display properties
        display_length, displacement = calc_display_area_props(self.screen_width,
                                                               self.screen_height)

        # Scale
        scale_resolution = get_ideal_image_resolution(display_length)
        self.scale_video_feed(scale_resolution)

        # Get image position
        max_img_size = display_length / 3
        img_positions = calculate_image_positions(display_length, max_img_size, max_img_size)

        # Apply displacement
        for _, value in img_positions.iteritems():
            value[0][0] += displacement
            value[1][0] += displacement

        # Calculate crop range
        crop_range = calculate_crop_range(scale_resolution, max_img_size)

        # Create master frame
        merged_frame = np.zeros((self.screen_height, self.screen_width, 3), dtype="uint8")

        # Name output window
        cv2.namedWindow("Output Window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Output Window", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

        while True:
            _, frame = self.video_feed.read()
            self.cropped_frame = frame[crop_range[0]:crop_range[1], crop_range[2]:crop_range[3]]
            frame_len = len(self.cropped_frame)
            t1 = threading.Thread(target=self.background_subtraction,
                                  args=[0, frame_len / 2, 0, frame_len / 2])
            t2 = threading.Thread(target=self.background_subtraction,
                                  args=[frame_len / 2, frame_len, 0, frame_len / 2])
            t3 = threading.Thread(target=self.background_subtraction, 
                                  args=[0, frame_len / 2, frame_len / 2, frame_len])
            t4 = threading.Thread(target=self.background_subtraction,
                                  args=[frame_len / 2, frame_len, frame_len / 2, frame_len])
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            '''pool = Pool(2)
            pool.map(self.background_subtraction, [0, frame_len / 2, 0, 1])
            pool.map(self.background_subtraction, [frame_len / 2, frame_len, 0, 1])
            pool.start()
            pool.join()'''
            #self.background_subtraction(0, frame_len, 0, frame_len)
            #cropped_frame = self.background_subtraction(cropped_frame)

            #http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
            for multipler, position_id in enumerate(IDENTIFIERS):
                merged_frame[img_positions[position_id][0][1]:
                             img_positions[position_id][1][1],
                             img_positions[position_id][0][0]:
                             img_positions[position_id][1][0]] = \
                                rotate_image_anticlockwise(self.cropped_frame, max_img_size,
                                                           90*multipler)

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


    def background_subtraction(self, col_start, col_end,
                               row_start, row_end):
        """
        Subtract the background colour (within a threshold) from a video frame 
        @param frame        :: The frame from the video
        @return the video frame minus the background
        """

        for column in range(col_start, col_end):
            for row in range(row_start, row_end):
                if (abs(self.cropped_frame[column][row][1] - self.background_colour[1]) <= self.threshold).all():
                    self.cropped_frame[column][row] = [0,0,0]
