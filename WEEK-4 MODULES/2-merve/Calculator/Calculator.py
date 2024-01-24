'''
Kullanıcı olarak temel matematik işlemlerini fonksiyonları kullanarak hesaplayabilen bir program kullanmak istiyorum. Böylece girdilerimi toplayabilir, çıkarabilir, çarpabilir veya bölebilirim. Kullanıcı çıkmak isteyene kadar kod her zaman çalışmalıdır. Kod hiçbir zaman çökmemelidir: kullanıcıdan bilgi alırken, hesaplama yaparken vs.

Kabul kriterleri:
Hesap makinesi Toplama, Çıkarma, Çarpma ve Bölme işlemlerini desteklemelidir.
Her biri için dört farklı dosyada dört modülü, parametre olarak iki kayan sayıyla tanımlayın.
Ve bu modülleri ana dosyanıza aktarmalısınız. Sonucu hesaplamak için math.ceil() işlevini kullanın ve 
sonuçtan daha büyük bir sonraki tam sayı değerini alın.
Print komutunu kullanarak ilgili seçeneklerle bir menü oluşturun ve kullanıcıdan bir giriş seçimi alın.
Durumlar için if/elif ifadelerini kullanın ve uygun işlevleri çağırın.
Çökmeleri önlemek için ana dosya ve modüllerdeki try/hariç blokları kullanın.
Kullanıcıya tekrar hesaplamak isteyip istemediğini sorun. 
Bunu uygulamak için y(evet) veya n(hayır) kullanıcısından girdi alın.
(matematik modülündeki import sys, ceil ve diğer hesaplama işlevlerini kullanın)

'''

import Addition, Division, Multiplication, Subtraction

while True:
    print('''
        Please press:
           
        for addition '+'
        for subtraction '-'
        for multiplication '*'
        for division '/' 
        for exit 'n'  
        ''')
    
    data=input()

    if data=='n':
        break

    try:
        x=float(input('first number:'))
        y=float(input('second number:'))
        Result = '' 
        if data=='+':
            Result = Addition.sum(x,y)

        elif data=='-':
            Result= Subtraction.extraction(x,y)

        elif data=='*':
            Result = Multiplication.multiply(x,y)

        elif data=='/':
            Result = Division.divide(x,y)
        
        else:
           print('You have logged in incorrectly. Please enter one of the options.') 
        print('Result ', Result)
    except ValueError:
        print('You have logged in incorrectly. Please enter a number.')

    
   

