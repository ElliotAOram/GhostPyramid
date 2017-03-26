"""module containing phrases for use in Charades game as well as helper functions"""
import unittest
from charades.phrases import get_phrases_from_type

class TestPhrases(unittest.TestCase):
    """
    Test phrase acquisition functions
    """

    ###===========================Success case==========================###
    def test_zero_phrase(self):
        output = get_phrases_from_type(0, 'ANIMAL')
        self.assertEqual(output, [])

    def test_one_animal_phrase(self):
        output = get_phrases_from_type(1, 'ANIMAL')
        self.assertEqual(output, ['animal'])

    def test_multi_animal_phrase(self):
        output = get_phrases_from_type(2, 'ANIMAL')
        self.assertEqual(output, ['animal', 'animal'])

    def test_one_sport_phrase(self):
        output = get_phrases_from_type(1, 'SPORT')
        self.assertEqual(output, ['sport'])

    def test_multi_sport_phrase(self):
        output = get_phrases_from_type(2, 'SPORT')
        self.assertEqual(output, ['sport', 'sport'])

    ###============================Failure cases========================###
    def test_negative_number(self):
        self.assertRaises(RuntimeError,
                          get_phrases_from_type,
                          -1, 'ANIMAL')

    def test_unknown_type(self):
        self.assertRaises(RuntimeError,
                          get_phrases_from_type,
                          1, 'NOT A TYPE')
