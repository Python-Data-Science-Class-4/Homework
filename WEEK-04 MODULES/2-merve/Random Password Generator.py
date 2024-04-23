'''
Kullanıcı olarak rastgele şifre üretip yazdırabilecek bir program kullanmak istiyorum. Böylece herhangi bir uygulama için şifremi oluşturabilirim.

Kabul kriterleri:
Şifre uzunluğu 10 ile 20 karakter arasında olmalıdır. Bu bilgiyi kullanıcıdan alın.
En az 2 büyük harf, 2 rakam ve 2 özel simge (noktalama işareti) içermelidir.
Tüm karakterleri karıştırmalısınız.
Çıktıda şifrelerin karakter sayıları da gösterilmelidir.
Kod bloklarının fonksiyonlarını anlatmak için yorum satırları yazmalısınız.
Gerekli bazı modülleri veya paketleri içe aktarmanız gerekir. (rastgele içe aktarma dizesini kullanın)

'''

#aciklama ve try except ekle.

import random, string

length=int(input('Please enter password length between 10 and 20:'))


digits=(random.choices(string.printable[0:11],k=2))
upper_case=(random.choices(string.printable[36:62],k=2))
special_symbols=(random.choices(string.printable[62:94],k=2))
remainder=(random.choices(string.printable,k=length-6))

result=(digits+upper_case+special_symbols+remainder)
random.shuffle(result)

password=''
for i in result:
    password+=i
print(f'''
Generated password:{password}
Password length:{len(password)}''')








# [print(len(string.printable))]

# print(string.printable.index("~"))

