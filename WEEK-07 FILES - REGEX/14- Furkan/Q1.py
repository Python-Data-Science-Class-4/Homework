
# Write a program that detects the ID number hidden in a text. 
# We know that the format of the ID number is: 
# 2letters, 1digit, 2letters, 2digits, 1letter, 1digit (: AA4ZA11B1).

import re
def detect_id (input_text):
    pattern = '[A-Z]{2}[0-9]{1}[A-Z]{2}[0-9]{2}[A-Z]{1}[0-9]{1}'
    
    match = re.findall(pattern, input_text)
    if match:
        return match[0]
    else:
        return None
    
input_text = input("To form the pattern, enter a string: ")
print("Input: ", input_text)

output = detect_id (input_text)
print("Output:", output)