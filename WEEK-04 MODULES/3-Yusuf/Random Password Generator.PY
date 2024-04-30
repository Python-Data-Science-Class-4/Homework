import random
import string

def password_creator():
    
    pw_length = int(input("How long a password do you want to generate? (between 10-20 characters): "))
    
    # All characters in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # requirements in the task
    num_uppercase = 2
    num_digits = 2
    num_special = 2

    # all in one 
    password_characters = (
        [random.choice(string.ascii_uppercase) for _ in range(num_uppercase)] +
        [random.choice(string.digits) for _ in range(num_digits)] +
        [random.choice(string.punctuation) for _ in range(num_special)] +
        [random.choice(all_characters) for _ in range(pw_length - (num_uppercase + num_digits + num_special))]
    )

    # change the places of the characters in the list
    random.shuffle(password_characters)

    # Liste içindeki karakterleri birleştirerek şifreyi oluştur
    generated_password = ''.join(password_characters)

    # Combining the characters in the list
    print(f"Oluşturulan Şifre: {generated_password}")
    print(f"Şifre Uzunluğu: {len(generated_password)} karakter")

# Call the fucntion.
password_creator()
