#Write a program that detects the ID number hidden in a text. 
#We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

import re

def id_number_detects(text):
    
    '''Created a pattern that helps to find ID like above'''
    pattern = (r'\w{2}\d\w{2}\d{2}\w\d')
    
    '''It detects the ID number from the text '''
    match_text = re.findall(pattern,text)
    
    if len(match_text) == 0:
        return "THERE IS NO ID IN THIS TEXT!"
    else:
        return match_text

try1 = "We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example:TY4KR45T6 AA4ZA11B1)."

output = id_number_detects(try1)

print("Output:",output)

