###########################################

import re

pattern = "\w\w\d\w\w\d\d\w\d"
string = input("Enter your text: ")

result = re.findall(pattern, string)
print(result)

###################################

#### example ######

string2= "AEGTV5VZ4PF94B6YH678"
result2 = re.findall(pattern, string2)
print(result2)