'''
Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 
2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6 Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678 Output : VZ4PF94B6
'''

import re

def id_number(data):
    pattern=re.compile(r"\w{2}\d{1}\w{2}\d{2}\w{1}\d{1}")
    id_number=pattern.search(data)
    print(f'ID Number: {id_number.group()}')

id_number('AEGTV5VZ4PF94B6YH678')
id_number('AABZA1111AEGTV5YH678MK4FM53B6')