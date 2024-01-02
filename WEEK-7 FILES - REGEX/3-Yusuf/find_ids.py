""" Question 1:
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
Input : AABZA1111AEGTV5YH678MK4FM53B6 Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678 Output : VZ4PF94B6 """

import re

#find 1 id.
def find_id_number(text):
    pattern = re.compile(r'[A-Z]{2}\d[A-Z]{2}\d{2}[A-Z]\d')
    match_result= pattern.search(text)
    if match_result:
        return match_result.group()
    else:
        return "No ID number found in the given text."

#find all ids in the text.    
def find_all_ids(text):
    pattern = re.compile(r'[A-Z]{2}\d[A-Z]{2}\d{2}[A-Z]\d')
    matches = pattern.findall(text)
    if matches:
        return matches
    else:
        return "No ID numbers found in the given text."
    
# Given texts
input_text1 = "AABZA1111AEGTV5YH678MK4FM53B6"
output1 = find_id_number(input_text1)
print("Input:", input_text1)
print("Output:", output1)

input_text2 = "AEGTV5VZ4PF94B6YH678"
output2 = find_id_number(input_text2)
print("\nInput:", input_text2)
print("Output:", output2)

input_text3= "ZA1111AEGTV5YH678KMK4FM537B6"
output3 = find_id_number(input_text3)
print("\nInput:", input_text3)
print("Output:", output3)

input_text4= "AABZA1111AEGTV5YH678MK4FM53B6 GTV5YH678KMK4FM537B6 AEGTV5VZ4PF94B6YH678"
output4 = find_all_ids(input_text4)
print("\nInput:", input_text4)
print("Output:", output4)