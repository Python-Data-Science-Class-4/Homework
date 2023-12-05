
import random
import string

n=int(input("Enter length of your password,between 10-20:"))

if 10 <n< 20:
    
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    '''Convert all characters to string and sum them as a characters'''
    characters = upper_letters + lower_letters + digits + punctuation
    password=[]
    '''create a list to add chrachters that given randomly from the for loop'''

    for i in range(n):
    
        password.append(random.choice(characters*2))
    
    password="".join(password)  #Convert to back as a string
    print(password,"Your password has",n,"characters")
else:
    print("Invalid range")


