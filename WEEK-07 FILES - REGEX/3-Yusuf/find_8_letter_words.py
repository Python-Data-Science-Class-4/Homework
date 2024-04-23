"""Question 2:
Search for eight-letter words within the text file 
named "eight_letter" located in the src folder 
and print them."""

#import os
import re
#print("Current Working Directory:", os.getcwd())
file_path = 'WEEK-7 FILES - REGEX/3-Yusuf/src/Eight_letter.txt'

def find_eight_letter_words_regex(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            eight_letter_words = re.findall(r'\b[A-Za-z]{8}\b', text)
            if eight_letter_words:
                return eight_letter_words
            else:
                return "No 8 letters word found."
    except FileNotFoundError:
        return f"File '{file_path}' not found."

result = find_eight_letter_words_regex(file_path)
print(result)
