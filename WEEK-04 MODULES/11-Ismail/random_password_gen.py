
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

'''Kod guzel ve calisiyor. Bir kac duzeltme yapabiliriz,.
**En basta n yerine daha anlasilir bir ifade yazabiliriz,password_length gibi.
**Neden (characters*2) kullandiginizi anlayamadim. Bu durumda bazı karakterlerin diğerlerinden daha fazla olasılıkla seçilmesine neden olabilir. 
Yani eğer characters içindeki bir karakter diğer karakterlere göre iki kat daha fazla tekrar ediyorsa o karakterin seçilme olasılığı iki kat daha yüksek olacaktır.
Her karakterin eşit olasılıkla seçilmesi icin random.choice(characters)) kullanmalisiniz.'''


