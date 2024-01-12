'''1 - Random Password Generator

As a user, I want to use a program which can generate random password and print it. So that I can generate my password for any application.

## Acceptance Criteria:
- Password length must between 10 and 20 characters long. Get this information from the user.
- It must contain at least 2 upper case letter, 2 digits and 2 special symbols (puncuations).
- You must mix all the characters.
- The output must be shown also the number of the passwords characters numbers.
- You must write comment lines for explaining the functions of the code bloks.
- You must import some required modules or packages. (use import random, string)'''

import string, random


def generate_password(length):
    # To meet the criteria, we need to be sure to generate at least 2 of the requested types. 
    # we use imported modules to reach the requested types and get random items 
    # below code will return random lists with item count of 2.
    two_uppers = random.choices(string.ascii_uppercase,k=2)
    two_digits = random.choices(string.digits,k=2)
    two_specials = random.choices(string.punctuation,k=2)
    
    # we need to also keep all possible charachters and select the remaining items from that list
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    remaining = random.choices(all_characters,k=(length-6))
    
    #then we combine all the selected items and use shuffle list operation.
    password = two_uppers + two_digits + two_specials + remaining
    random.shuffle(password)

    # we return the list as a string using join
    return "".join(password)

# to make sure length is within limit and user entered integer, we apply below code
while True:
    try: 
        password_length = int(input("Please write the length of password between 10 and 20."))
        if 10<=password_length<=20:
            break
        else:
            print("Length must be between 10 and 20 characters.")
    except ValueError:
            print("Please enter a valid number.")

    
# we call our function and print the result
generated = generate_password(password_length)
print(f"Generated Password: {generated}")
print(f"Number of characters in the password: {len(generated)}")