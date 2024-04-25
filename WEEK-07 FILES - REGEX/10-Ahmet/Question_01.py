import re

pattern = (r'\w{2}\d{1}\w{2}\d{2}\w{1}\d{1}')       # We defined our pattern
input = input("Please enter a pattern:")            # We asked the user for the input text.
result = re.findall(pattern, input)                 # We searched for our pattern in the text using "re.findall".
print(f"İnput : {input}\nOutput : {result[0]}")     # We printed the result.