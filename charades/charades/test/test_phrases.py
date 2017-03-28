"""module containing phrases for use in Charades game as well as helper functions"""
import unittest
from charades.phrases import get_phrases_from_type

class TestPhrases(unittest.TestCase):
    """
    Test phrase acquisition functions
    """

    ###===========================Success case==========================###
    def test_zero_phrase(self):
        output = get_phrases_from_type(0, 'ANIMALS')
        self.assertEqual(output, [])

    def test_one_animal_phrase(self):
        output = get_phrases_from_type(1, 'ANIMALS')
        self.assertEqual(len(output), 1)

    def test_multi_animal_phrase(self):
        output = get_phrases_from_type(2, 'ANIMALS')
        self.assertEqual(len(output), 2)

    def test_one_sport_phrase(self):
        output = get_phrases_from_type(1, 'SPORTS')
        self.assertEqual(len(output), 1)

    def test_multi_sport_phrase(self):
        output = get_phrases_from_type(2, 'SPORTS')
        self.assertEqual(len(output), 2)

    def test_max_five(self):
        output = get_phrases_from_type(7, 'ANIMALS')
        self.assertEqual(len(output), 5)

    def test_any_type(self):
        output = get_phrases_from_type(5, 'ANY')
        self.assertEqual(len(output), 5)

    def test_none_same(self):
        output = get_phrases_from_type(5, 'ANIMALS')
        for idx, current_phrase in enumerate(output):
            sub_output = output
            sub_output.pop(idx)
            for next_phrase in sub_output:
                self.assertNotEqual(current_phrase, next_phrase)

    def test_check_valid_phrase(self):
        self.assertTrue(check_phrase('Tennis'))

    def test_check_valid_phrase_lower(self):
        self.assertTrue(check_phrase('tennis'))

    def test_check_valid_phrase_upper(self):
        self.assertTrue(check_phrase('TENNIS'))

    def test_check_valid_phrase_mixed_case(self):
        self.assertTrue(check_phrase('TeNNiS'))

    def test_check_invalid_phrase(self):
        self.assertFalse(check_phrase('Test phrase'))


    ###============================Failure cases========================###
    def test_negative_number(self):
        self.assertRaises(RuntimeError,
                          get_phrases_from_type,
                          -1, 'ANIMALS')

    def test_unknown_type(self):
        self.assertRaises(RuntimeError,
                          get_phrases_from_type,
                          1, 'NOT A TYPE')
