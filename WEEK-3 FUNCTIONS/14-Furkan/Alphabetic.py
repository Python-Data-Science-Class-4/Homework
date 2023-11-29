def colours(input_clr):
    
    # Join the sorted words with hyphens between them
    output_clr = '-'.join(x)

    return output_clr

# Example usage:

clr_1 = input ("Your favourite colour?: ")
clr_2 = input ("Second choice: ")
clr_3 = input ("Third choice: ")

input_clr = clr_1,clr_2,clr_3
x = sorted (input_clr)
output_clr = colours(x)

print(f'''Input   : {input_clr}
Output  : {output_clr}''')

''' Kod mantik olarak guzel ve dogru calisiyor ama bir kac duzeltme yapmamiz gerekiyor.
**'colours' fonksiyonu 'input_clr' adlı bir parametre almalı, 
ama siz fonksiyonu çağırırken x değişkenini kullanıyorsunuz.Fonksiyon çağrısını düzeltebiliriz.
**input_clr'yi tanımlarken virgülle ayrılmış bir demet oluşturmalısınız 
(input_clr = (clr_1, clr_2, clr_3)). 
Şu anda input_clr bir demet değil üç ayrı değişkeni içeren bir tuple.'''
