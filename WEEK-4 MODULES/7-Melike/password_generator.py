


import random
import string


len_password = int(input(("How many characters do you want a password?(10 to 20): ")))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
all_chars = lower + upper + digits + special

password = ""

for i in range(2):
    password += ''.join(random.choice(upper))
for i in range(2):
    password += ''.join(random.choice(digits))
for i in range(2):
    password += ''.join(random.choice(special))

remaining = len_password- 6 # Number of characters remaining after the above selections are made

for i in range(remaining):
    password += ''.join(random.choice(all_chars))


password = list(password)
random.shuffle(password) #
print("Your password :", ''.join(password))

print("Character length of your password:",len(password))



