"""Helper functions for vpa"""
import ctypes
from cv2 import getRotationMatrix2D, warpAffine
from parsers import parse_positive_int, parse_non_zero_int
from sys import platform

if sys.platform == "linux":
    import gtk, pygtk

RESOLUTIONS = [(1920, 1080), (1280, 720), (960, 540),
               (640, 480), (320, 240), (424, 240), (320, 180)] # May add more to support mobile

def get_screen_resolution():
    """
    Returns the screen width and height as a tuple.
    @return     :: (screen_width, screen_height)
    """
    if sys.platform == "win32":
        #http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
        user32 = ctypes.windll.user32
        return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    elif sys.platform == "linux"
        window = gtk.Window()
        screen = window.get_screen()
        return (screen.get_width(), screen.get_height())
    else:
        return (1920, 1080)


def calc_display_area_props(width, height):
    """
    Calculates the largest possible square and its co-ordinates in a
    provided rectangular space. This is used to establish the correct
    display area on a screen
    @param width        :: Width of screen
    @param height       :: Height of screen
    @return             :: display_length and displacement from screen edge (0,0)
    @raises ValueError  :: If any input is non integer or zero
    """
    #parse input and get default screen size if not provided
    parse_non_zero_int(width)
    parse_positive_int(width)
    parse_non_zero_int(height)
    parse_positive_int(height)

    # Assume width > height (most monitors)
    display_length = height
    displacement = (width - display_length) / 2   # Indent from side/top of screen
    if width < height:
        display_length = width
        displacement = (height - display_length) / 2

    return display_length, displacement



def calculate_image_positions(display_length, width, height):
    """
    Calculates the positions (origin, bottom right) for each image in the
    output window.
    @param display_length   :: Length of one side of the display area.
                               Area assumed to be square
    @param width            :: Width of the image
    @param height           :: Height of the image
    @return                 :: A dictionary of image postions by origin
                               and bottom right tuples - for example:
                               {"top": [(25,0), (75,50)]
                                "left ": [...]}
    """
    # Parse input
    arguements = locals()
    for _, value in arguements.iteritems():
        parse_non_zero_int(value)
        parse_positive_int(value)

    # Find half values
    h_image_width = width / 2
    h_image_height = height / 2
    h_side_length = display_length / 2

    # Define markers
    first_width = h_side_length-h_image_width
    second_width = h_side_length+h_image_width
    first_height = h_side_length-h_image_height
    second_height = h_side_length+h_image_height


    return {"top"   : [[first_width, 0], [second_width, height]],
            "left"  : [[0, first_height], [width, second_height]],
            "bottom": [[first_width, display_length-height], [second_width, display_length]],
            "right" : [[display_length-width, first_height], [display_length, second_height]]
           }


def get_ideal_image_resolution(display_length):
    """
    Takes the display length and works out the next largest resolution to scale
    the video to where: display length / 3 > resolution.width && resolution.height
    """
    parse_non_zero_int(display_length)
    parse_positive_int(display_length)
    max_image_size = display_length / 3
    max_res = (320, 180)
    for index in range(0, len(RESOLUTIONS)):
        if max_image_size >= RESOLUTIONS[index][1]:
            if RESOLUTIONS[index][1] > max_res[1]:
                max_res = RESOLUTIONS[index-1]
    return max_res


def calculate_crop_range(scale_resolution, max_img_size):
    """
    Calculates the correct cropping range for the image to make it square
    @param scale_resolution     :: The current resolution of the image
    @param max_img_size         :: Largest possible size for the image
    @return a list of value to crop by such that an image is cropped by:
            img = img[crop_range[0]:crop_range[1], crop_range[2]:crop_range[3]]
    """
    parse_non_zero_int(scale_resolution[0])
    parse_non_zero_int(scale_resolution[1])
    parse_positive_int(scale_resolution[0])
    parse_positive_int(scale_resolution[1])
    parse_non_zero_int(max_img_size)
    parse_positive_int(max_img_size)

    central_width = scale_resolution[0] / 2
    central_height = scale_resolution[1] / 2
    h_image_max = max_img_size / 2
    # [h_start, h_end, v_start, v_end]
    return [central_height - h_image_max, central_height + h_image_max,
            central_width - h_image_max, central_width + h_image_max]


def rotate_image_anticlockwise(frame, sq_img_size, degrees):
    """
    Rotates a square image clockwise by a given number of degrees.
    This function will not perform additional object parsing for effeciency.
    @param frame        :: the frame to manipulate
    @param sq_img_size  :: the size of the image (imae must be square)
    @degrees            :: the number of degrees to rotate by (clockwise)
    @return rotated_frame
    """
    rot_matrix = getRotationMatrix2D((sq_img_size/2, sq_img_size/2), degrees, 1)
    rotated_frame = warpAffine(frame, rot_matrix, (sq_img_size, sq_img_size))
    return rotated_frame
