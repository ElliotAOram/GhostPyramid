"""Module that stores phrases and handles random phrase selection"""
from random import randint

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Mouse', 'Meerkat', 'Kangaroo', \
           'Monkey', 'Frog', 'Penguin', 'Bird']

SPORTS = ['Tennis', 'Football', 'Swimming', 'Rowing', 'Karate', 'Rugby', 'Shot put', \
          'Skipping']

ACTIVITY = ['Brushing Teeth', 'Combing Hair', 'Sweeping', 'Sleeping']

TYPES = ['ANIMALS', 'SPORTS', 'ACTIVITY', 'ANY']


def find_list(list_type):
    """
    Return the desire list from the type variable
    @param list_type    :: The type of list to find
    """
    if list_type == 'ANY':
        return ANIMALS + SPORTS + ACTIVITY
    return {
        'ANIMALS': ANIMALS,
        'SPORTS': SPORTS,
        'ACTIVITY': ACTIVITY,
    }[list_type]

def check_phrase(phrase):
    """
    Ensures that the phrase is known and valid
    @param the phrase to check
    @return category if valid else return false
    """
    if phrase.upper() in [x.upper() for x in ANIMALS]:
        return 'Animal'
    if phrase.upper() in [x.upper() for x in SPORTS]:
        return 'Sport'
    if phrase.upper() in [x.upper() for x in ACTIVITY]:
        return 'Activity'
    return False

def get_phrases_from_type(num_of_items, list_type):
    """
    Gets a number of phrases from a given category.
    Check that the type of list can be found and the number of items is not 0 (or less)
    @param num_of_items     :: The number of items to return
    @param list_type        :: The name of the list to find
    @return list of phrases
    """
    if list_type not in TYPES:
        raise RuntimeError('Type %s is not one of the available types of phrase.' % (list_type))
    if num_of_items > 5:
        num_of_items = 5
    if num_of_items < 0:
        raise RuntimeError('The number of item, %d, must be positive number.' % (num_of_items))
    category_list = find_list(list_type)
    phrases = []
    used_numbers = []
    for _ in range(0, num_of_items):
        index = randint(0, len(category_list)-1)
        while index in used_numbers:
            index = randint(0, len(category_list) -1)
        phrases.append(category_list[index])
        used_numbers.append(index)
    return phrases
