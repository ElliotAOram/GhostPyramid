"""object parsers to ensure type safety in python"""

def parse_int(parser_input):
    """
    Checks input is an integer
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int
    @return             :: True if input is int
    """
    try:
        int(parser_input)
        return True
    except ValueError:
        raise ValueError('Value provided is not an integer')

def parse_positive_int(parser_input):
    """
    Checks input is an integer and positive
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int or non-positive
    @return             :: True if input is int
    """
    int(parser_input)
    if parser_input >= 0:
        return True
    else:
        raise ValueError('Value provided is not positive')

def parse_non_zero_int(parser_input):
    """
    Checks input is an integer and non_zero
    @param input        :: the input to be checked
    @raises ValueError  :: If non-int or zero
    @return             :: True if input is int
    """
    int(parser_input)
    if parser_input == 0:
        raise ValueError('Value provided can not be zero')
    else:
        return True
