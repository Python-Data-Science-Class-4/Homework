#Random Password Generator
import random
import string
while True :
    
    try:
        len_passwords = int(input('Your password must be between 10 and 20 characters. How many characters is the password? '))
        if len_passwords < 10 or len_passwords > 20:
            raise ValueError("Please enter a number between 10 and 20.")
        break  # Exits the loop when a correct value is received.
    except ValueError as e:
        print(e)
while True :       
    
    punct = string.punctuation
    digits = string.digits
    letters =string.ascii_lowercase
    let_upper = string.ascii_uppercase
    new_list = punct+digits+letters+let_upper 
    password = [random.sample(punct,2),random.sample(digits,2),random.sample(let_upper,2),random.sample(new_list,len_passwords-6)]
    password = sum(password,[])
    random.shuffle(password)
    password = ''.join(password)
    password = f'password:{password}'
    print(password)
    print('password_len :',len(password))
    answer = input("Do you want to get a new password?: 'yes' or 'no'" )
    if answer.lower() != 'yes':
        break
        




