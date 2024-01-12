import re


input = input("Please enter text containing email addresses: ")

pattern = r"\S+@\S+"    # We defined our pattern
split = "@"             # We set the "@" sign as our split character.
name = []

match = re.findall(pattern, input)  # We took the parts that fit our pattern in the text entered from input.

print (match)

for i in match: 
    name.append(re.split(split,i)[0])   # We divided each element in the "match" variable from the character we specified in the split and saved the first element in the "name" list.

print(name)