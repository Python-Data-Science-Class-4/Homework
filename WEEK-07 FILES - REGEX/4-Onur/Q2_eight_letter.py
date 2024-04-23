"""
## Question 2:
Search for eight-letter words within the text file named "eight_letter" located in the src folder and print them.
"""

import re

# our currency directory is Homework so the file location will be like below. 
path = 'WEEK-7 FILES - REGEX/src/eight_letter.txt'

with open(path, 'r') as file:
    text = file.read()

# in order to get exact 8-letter words we need to use \b 
pattern = r'\b[A-Za-z]{8}\b'

words = re.findall(pattern,text)

# we print the results with for loop
print("Eight letter words in the file are: ")
for word in words:
    print(word)