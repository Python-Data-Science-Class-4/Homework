import string
import random

def password_generator():
    while True: # take the length of password, try till the input is valid
        try:
            password_len = int(input('Please enter a number between 10 and 20: '))
            if password_len >= 10 and password_len <= 20: # check if the input is between 10 and 20
                break
            else:
                print('Invalid input')
        except TypeError: #check if the input type is integer
            print('Invalid input')

    generated_password = (
        random.choices(string.ascii_uppercase, k=2) + # at least 2 uppercase, 2 digits and 2 punctuation
        random.choices(string.digits, k=2) +
        random.choices(string.punctuation, k=2) +
        random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_len-6) # take the remain characters
    )

    random.shuffle(generated_password) # shuffle the characters in a random order

    return "".join(generated_password)

new_psw = password_generator()
print(f'Generated Password: {new_psw}')
print(f'Password Length: {len(new_psw)}')

'''Kod gayet guzel,dogru calisiyor ve isteneni veriyor ama bir kac duzeltmeyapabiliriz.
**'TypeError' genellikle farklı türde bir işlem yapılmaya çalışıldığında ortaya çıkar.
Kullanıcının sayı girmesini sağlamak ve bu sayıyı almak istediğimizde 'ValueError' kullanmamız daha uygun olur.'''






    
         
