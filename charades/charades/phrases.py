"""Module that stores phrases and handles random phrase selection"""
from random import randint

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Mouse', 'Meerkat', 'Kangaroo', 'Monkey', 'Frog', 'Penguin', 'Bird']

SPORTS = ['Tennis', 'Football', 'Swimming', 'Rowing', 'Karate', 'Rugby']

TYPES = ['ANIMALS', 'SPORTS', 'ANY']


def find_list(type):
    """
    Return the desire list from the type variable
    @param the type of list to find
    """
    if type == 'ANY':
        return ANIMALS + SPORTS
    return {
        'ANIMALS': ANIMALS,
        'SPORTS': SPORTS,
    }[type]

def check_phrase(phrase):
    """
    Ensures that the phrase is known and valid
    @param the phrase to check
    @return true is valid
    """
    all_phrases = ANIMALS + SPORTS
    return phrase.upper() in [x.upper() for x in all_phrases]

def get_phrases_from_type(num_of_items, type):
    if type not in TYPES:
        raise RuntimeError('Type %s is not one of the available types of phrase.' % (type))
    if num_of_items > 5:
        num_of_items = 5
    if num_of_items < 0:
        raise RuntimeError('The number of item, %d, must be positive number.' % (num_of_items))
    list = find_list(type)
    phrases = []
    used_numbers = []
    for _ in range(0, num_of_items):
        index = randint(0, len(list)-1)
        while index in used_numbers:
            index = randint(0, len(list) -1)
        phrases.append(list[index])
        used_numbers.append(index)
    return phrases
