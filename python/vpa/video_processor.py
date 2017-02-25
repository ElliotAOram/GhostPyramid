"""Contains the VideoProcessor class (core application)"""
import cv2
from helper_functions import get_screen_width_and_height, calculate_screen_boundaries, \
                             get_ideal_image_resolution, create_image_position_dict
import numpy as np
from parsers import parse_positive_int


INDENTIFIERS = ["top", "left", "bottom", "right"]


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
        parse_positive_int(device)
        self.video_feed = cv2.VideoCapture(device)


    def end_capture(self):
        """
        Ends capturing video from the current video_feed.
        Sets the video_feed object make to None to avoid misuse.
        """
        self.video_feed.release()
        self.video_feed = None

    def process_and_output_video(self):
        """
        Outputs all video_feeds to a single output window
        """
        # Establish image and monitor dimensions
        screen_res = get_screen_width_and_height()
        display_area = calculate_screen_boundaries(screen_res[0], screen_res[1])

        # Scale video feed to the largest resolution that is still valid
        display_side_length = abs(display_area[1][1] - display_area[0][1])
        scale_resolution = get_ideal_image_resolution(display_side_length)
        self.video_feed.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, scale_resolution[0])
        self.video_feed.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, scale_resolution[1])

        # Get image position
        maximum_img_size = display_side_length / 3
        img_positions = create_image_position_dict(screen_res[0], screen_res[1],
                                                   maximum_img_size, maximum_img_size)

        # Calculate crop range
        central_width = scale_resolution[0] / 2
        central_height = scale_resolution[1] / 2
        h_image_max = maximum_img_size / 2
        # [h_start, h_end, v_start, v_end]
        crop_range = [central_height - h_image_max, central_height + h_image_max,
                      central_width - h_image_max, central_width + h_image_max]

        #http://stackoverflow.com/questions/17696061
        #/how-to-display-a-full-screen-images-with-python2-7-and-opencv2-4
        cv2.namedWindow("Output Window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Output Window", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

        while True:
            _, frame = self.video_feed.read()
            cropped_frame = frame[crop_range[0]:crop_range[1], crop_range[2]:crop_range[3]]
            #http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
            merged_frame = np.zeros((screen_res[1], screen_res[0], 3), dtype="uint8")

            for multipler, position_id in enumerate(INDENTIFIERS):
                rot_matrix = cv2.getRotationMatrix2D((maximum_img_size/2, maximum_img_size/2),
                                                     90*multipler, 1)
                rotated_frame = cv2.warpAffine(cropped_frame, rot_matrix,
                                               (maximum_img_size, maximum_img_size))
                merged_frame[img_positions[position_id][0][1]:
                             img_positions[position_id][1][1],
                             img_positions[position_id][0][0]:
                             img_positions[position_id][1][0]] = rotated_frame

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
