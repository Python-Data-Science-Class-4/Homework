#####################################

import re

pattern = r"\w{8}"

with open ("C:\Users\umut\Documents\GitHub\Homework\WEEK-7 FILES - REGEX\src", 'r', encoding = "utf_8") as file:
    text = file.read()

eight_letter = re.findall(pattern, text)
print(eight_letter)

##########################################