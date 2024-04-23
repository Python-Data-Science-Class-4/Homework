'''
Search for eight-letter words within the text file named 
"eight_letter" located in the src folder and print them
'''

import re
with open(r'C:\Users\Gebruiker\Documents\GitHub\Homework\WEEK-7 FILES - REGEX\src\eight_letter.txt', 'a+') as my_file:
    my_file.seek(0)
    result=re.findall(r"\w{8}",my_file.readline())
    print(result)



# os.makedirs(r"C:\Users\Gebruiker\Desktop\Python\Week7\src")
# eight_letter=r"C:\Users\Gebruiker\Desktop\Python\Week7\src\eight_letter.txt"