# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:37:03 2023

@author: aksha
"""

import unittest
from Number_Converter_function import Number_to_word  # Import the function to be tested

class TestNumberToWords(unittest.TestCase):
    """
    A test suite for the Number_to_word function.
    """

    def test_valid_numbers(self):
        """
        Test cases for valid input within the specified range (0 to 100).
        """
        self.assertEqual(Number_to_word(0), "zero")
        self.assertEqual(Number_to_word(1), "one")
        self.assertEqual(Number_to_word(10), "ten")
        self.assertEqual(Number_to_word(19), "nineteen")
        self.assertEqual(Number_to_word(20), "twenty")
        self.assertEqual(Number_to_word(22), "twenty-two")
        self.assertEqual(Number_to_word(100), "one hundred")

    def test_out_of_range(self):
        """
       Test cases for out-of-range input.
       """
       
        self.assertEqual(Number_to_word(-1), "Number out of range (0-100)")
        self.assertEqual(Number_to_word(101), "Number out of range (0-100)")
        
    def test_string_input(self):
        """
       Test cases for string input (invalid input).
       """
       
        self.assertEqual(Number_to_word("string"), "Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    unittest.main()

