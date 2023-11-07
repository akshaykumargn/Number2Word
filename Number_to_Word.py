#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:20:31 2023

@author: aksha
"""
import sys

# Import the function you want to use
from Number_Converter_function import Number_to_word, get_input 
from test_NumberConverter import TestNumberToWords  # Import your test runner function

def main():
    """
    The main function of the application.
    It obtains user input, converts the input number to words, and runs unit tests.
    """
    if len(sys.argv) != 3:
        print("Invalid Input")
        print("Usage: main.py <integer>")
        return

    try:
        n = int(sys.argv[-1])
        num = get_input(n)
        result = Number_to_word(num)  # Use your function
        print(f"{result}")

    except ValueError:
        print("Invalid input. Please provide a valid integer.")
        
    TestNumberToWords()  # Run your unit tests  
    
if __name__ == "__main__":
    main()