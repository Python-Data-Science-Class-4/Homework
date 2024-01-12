"""
## Question 1:
Write a program that detects the ID number hidden in a text.
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit
(For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
"""

import re

def detect_id (string):
    # we use regex pattern to match the desired order. it is assumed that the letter could be upper or lowercase.
    pattern = '[A-Za-z]{2}\d[A-Za-z]{2}\d{2}[A-Za-z]\d'
    match = re.search(pattern, string)
    # in order to print the matched string we need to use group function.
    print(f'Input: {string}\nOutput: {match.group()}')

user_input = input("Please write a string to extract id number")

detect_id(user_input)
