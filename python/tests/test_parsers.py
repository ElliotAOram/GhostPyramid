"""Tests for object parsers"""
import unittest

from .context import vpa

class TestPositiveParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """
    ###---------------------------------Success cases----------------------------------###
    def test_zero(self):
        self.assertTrue(vpa.parse_positive_int(0))

    def test_positive(self):
        self.assertTrue(vpa.parse_positive_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_negative(self):
        self.assertRaises(ValueError,
                          vpa.parse_positive_int,
                          -1)

class TestNonZeroParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      non zero integers
    """

    ###---------------------------------Success cases----------------------------------###
    def test_negative(self):
        self.assertTrue(vpa.parse_non_zero_int(-10))

    def test_positive(self):
        self.assertTrue(vpa.parse_non_zero_int(10))

    ###---------------------------------Failure cases-----------------------------------###

    def test_zero(self):
        self.assertRaises(ValueError,
                          vpa.parse_non_zero_int,
                          0)

class TestIntParser(unittest.TestCase):
    """
    @class TestPositiveParser      :: Tests that ensure the input parser only accepts
                                      postive integers
    """

    ###---------------------------------Success cases----------------------------------###
    def test_integer_zero(self):
        self.assertTrue(vpa.parse_int(0))


    def test_negative(self):
        self.assertTrue(vpa.parse_int(-1))

    ###---------------------------------Failure cases-----------------------------------###

    def test_non_int(self):
        self.assertRaises(ValueError,
                          vpa.parse_int,
                          "Non int")
