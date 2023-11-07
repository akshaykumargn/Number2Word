# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:01:48 2023
@author: aksha
"""

def Number_to_word(n):
    """
    Convert a given number to its word representation.

    Args:
        n (int): The number to be converted.

    Returns:
        str: The word representation of the number or an error message if the input is out of range.

    Example:
        Number_to_word(42) returns "forty-two"
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
    Get user input for a number between 0 and 100.

    Args:
        n (int): The number entered by the user.

    Returns:
        int: The valid number entered by the user within the specified range.

    Example:
        get_input(42) returns 42
    """
    while True:
        try:
            # n = int(input("Enter a number between 0 and 100: "))
            if 0 <= n<= 100:
                return n
            else:
                print("Number out of range. Please enter a number between 0 and 100.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
