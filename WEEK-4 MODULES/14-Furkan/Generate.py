import random
import string

def new(length):

    upper   = string.ascii_uppercase  
    lower   = string.ascii_lowercase 
    numeral = string.digits 
    punct   = string.punctuation
    
    pw = [random.choice(upper)*2,random.choice(numeral)*2,random.choice(punct)*2]
    
    length = max(10, min(length, 20))
     
    together = length - len(pw) - 3      # For the formulization I had to use '3'
    characters = upper + lower + numeral + punct
    pw.extend(random.choice(characters) for x in range(together))
    random.shuffle (pw)
    return ''.join(pw)
    
def create():
    password_length = int(input("Enter the number of password between 10-20: "))
    password = new(password_length)
    
    if password_length >=10 and password_length <=20:
        print(f"Generated password: {password}")
        print(f"Password length: {len(password)} characters")
    else:
        print("The number you gave is wrong.")

create()