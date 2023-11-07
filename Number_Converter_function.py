# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:01:48 2023
@author: aksha
"""

def Number_to_word(n):
    """
    Convert a given number to its word.

    Args:
        n (integer): The input to be converted.

    Outputs:
        string: The word representation of the input integer or an error message if the input is out of range.

    Example:
        Number_to_word.py 55 returns "fifty-five"
    """
    if isinstance(n, int):
        units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        
        if 0 <= n <= 19:
            return units[n]
        elif 20 <= n <= 99:
            return tens[n // 10] + ("-" + units[n % 10] if n % 10 != 0 else "")
        elif n == 100:
            return "one hundred"
        else:
            return "Number out of range (0-100)"

    else:
        return "Invalid input. Please enter a valid number."
    
def get_input(n):
    """
    Obtain input for a number between 0 and 100.

    Args:
        n (integer): The input by the user.

    Outputs:
        integer: The valid input entered by the user within the accepted range.

    Example:
        get_input(42) returns 42
    """
    while True:
        try:
            if 0 <= n<= 100:
                return n
            else:
                print("Number out of range. Please enter a number between 0 and 100.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
