given_list=[1,2,3,3,3,3,3,3,4,5,5,5]
unique_list=[]
def num_filter (given_list):
    i=0
    for i in given_list:
        if i not in unique_list:
            ''' Checking every single variable in the given_list. if variables not in the list then add to unique list'''
            unique_list.append(i)
    print(unique_list)    
    return
    
    
print(num_filter(given_list))

''' Kod iyi ancak bazi gelistirmeler yapabiliriz.
**Herhangi bir fonksiyon icinde olusturulan degisken 'local variable' olarak adlandirilir,
fonksiyon disindaki variable'lar ise 'global variable' olarak adlandiriyoruz. 
Fonksiyon içinde global bir değişkeni (burada unique_list) kullanmak genellikle iyi bir uygulama değildir. 
Fonksiyonlar genellikle bağımsız ve kendi içerdikleri değişkenleri kullanmalıdır. 
Bu durumda, fonksiyona parametre olarak given_listi geçirebilir ve işlem sonucunu geri döndürebilirsiniz.

**Fonksiyonunuz şu anda bir şey döndürmüyor,bu nedenle return ifadesine unique_list i ekleyebilirsiniz

**Dongu kullanmadan set() ile de unique elemanlari bulabiliriz. 
Once set() ile liste elemanlari tekrardan kurtulur, sonra sorted() ile liste halinde sirali dondurulebilir.
Alternatif bir cozum sundum, inceleyebilirsiniz.

letters = ["a","z","b","c","c","d","f","e","e","g","h","h","j"]

def unrepeated(first_list):
    last_list = sorted(set(first_list))
    return last_list

print(unrepeated(letters)) '''
