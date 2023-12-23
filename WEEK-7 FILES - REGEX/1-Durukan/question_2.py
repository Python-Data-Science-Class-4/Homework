## Question 2:
# Search for eight-letter words within the text file named 
# "eight_letter" located in the src folder and print them.

import re

pattern = re.compile(r"\b\w{8}\b")

with open("./WEEK-7 FILES - REGEX/src/eight_letter.txt", "r") as readFile:
    data = readFile.read()
    words = pattern.findall(data)

for i in words:
    print(i)