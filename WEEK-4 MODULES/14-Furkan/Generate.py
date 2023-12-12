import random
import string

def new(length):
    upper   = string.ascii_uppercase  
    lower   = string.ascii_lowercase 
    numeral = string.digits 
    punct   = string.punctuation
    
    pw_1 = [random.choice(upper),random.choice(numeral),random.choice(punct),
            random.choice(upper),random.choice(numeral),random.choice(punct)]
    # Criteria: a) Password length between 10-20   b) At least 2 upper, 2 lower, 2 symbols 
    length = max(10, min(length, 20))
     
    len_of_others = length - len(pw_1)     
    other_characters = []
    for x in range(len_of_others):
        other_characters += random.choice(lower)
    pw_1.extend(other_characters)
    random.shuffle (pw_1)
    return ''.join(pw_1)
    
def create():
    password_length = int(input("Enter the number of password between 10-20: "))
    password = new(password_length)
    
    if password_length >=10 and password_length <=20:
        print(f"Generated password: {password}")
        print(f"Password length: {len(password)} characters")
    else:
        print("The number you gave is wrong.")

create()
