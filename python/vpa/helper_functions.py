"""Helper functions for vpa"""
import ctypes

###================================Parser functions========================###
def parse_int(input):
    """
    Checks input is an integer
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int
    @return             :: True if input is int
    """
    try:
        int(input)
        return True
    except ValueError:
         raise ValueError('Value provided is not an integer')

def parse_positive_int(input):
    """
    Checks input is an integer and positive
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int or non-positive
    @return             :: True if input is int
    """
    parse_int(input)
    if input >= 0:
        return True
    else:
        raise ValueError('Value provided is not positive')

def parse_non_zero_int(input):
    """
    Checks input is an integer and non_zero
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int or zero
    @return             :: True if input is int
    """
    parse_int(input)
    if input == 0:
        raise ValueError('Value provided can not be zero')
    else:
        return True

###=================================VPA Helper functions=================###

def get_screen_width_and_height():
    """
    Returns the screen width and height as a tuple.
    @return     :: (screen_width, screen_height)
    """
    #http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    user32 = ctypes.windll.user32
    return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


def calculate_screen_boundaries(width=None, height=None):
    """
    Calculates the largest possible square and its co-ordinates in a
    provided rectangular space. This is used to establish the correct
    display area on a screen
    @param width        :: default = None - Max width of the screen. 
                           If not provided use screen resolution
    @param height       :: default = None - Max height of the screen. 
                           If not provided use screen resolution
    @return             :: Tuple representing the origin and bottom right
                           hand corner of the display area
    @raises ValueError  :: If any input is non integer or zero
    """
    #parse input and get default screen size if not provided

    if width is None:
        width = get_screen_width_and_height()[0]
    else:
        parse_non_zero_int(width)
        parse_positive_int(width)

    if height is None:
        height = get_screen_width_and_height()[1]
    else:
        parse_non_zero_int(height)
        parse_positive_int(height)

    # Assume width > height (most monitors)
    square_side = height
    displacement = (width - square_side) / 2   # Indent from side/top of screen
    if width < height:
        square_side = width
        displacement = (height - square_side) / 2
        return [(0,displacement),(width, height-displacement)]
    else:
        return [(displacement,0),(width-displacement, height)]



def calculate_image_positions(side_length, width, height):
    """
    Calculates the positions (origin, bottom right) for each image in the 
    output window.
    @param side_length      :: Length of one side of the display area.
                               Area assumed to be square
    @param width            :: Width of the image
    @param height           :: Height of the image
    @return                 :: A dictionary of image postions by origin 
                               and bottom right tuples - for example:
                               {"top": [(25,0), (75,50)]
                                "left ": [...]}
    """
    # Parse input
    parse_non_zero_int(side_length)
    parse_non_zero_int(width)
    parse_non_zero_int(height)
    parse_positive_int(side_length)
    parse_positive_int(width)
    parse_positive_int(height)
    
    # Find half values
    h_image_width = width / 2
    h_image_height = height / 2
    h_side_length = side_length / 2
    
    # Define markers
    first_width = h_side_length-h_image_width
    second_width = h_side_length+h_image_width
    first_height = h_side_length-h_image_height
    second_height = h_side_length+h_image_height
    
    
    return {"top"   : [[first_width, 0] , [second_width, height]],
            "left"  : [[0, first_height], [width, second_height]],
            "bottom": [[first_width, side_length-height],[second_width, side_length]],
            "right" : [[side_length-width, first_height],[side_length, second_height]]
           }
    
def create_image_position_dictionary(screen_width, screen_height, frame_width, frame_height):
    """
    Calculates the position dictionary for images given a screen
    size and image size. Applies the displaces changes to the dictionary
    to postion images based on display size.
    """
    # Parse input
    arguements = locals()
    for _, v in arguements.iteritems():
        parse_non_zero_int(v)
        parse_positive_int(v)

    # Feed into functions to calculate display area and image positions
    display_area = calculate_screen_boundaries(screen_width, screen_height)
    display_side_length = abs(display_area[1][1] - display_area[0][1])
    displacement = max(display_area[0][0], display_area[0][1])

    img_positions = calculate_image_positions(display_side_length,
                                              frame_width, frame_height)

    # Apply displacement
    for _, value in img_positions.iteritems():
        value[0][0] += displacement
        value[1][0] += displacement
    
    return img_positions
