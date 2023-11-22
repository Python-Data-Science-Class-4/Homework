'''Kullanýcýdan gelen bir cümleyi giren ve ardýndan her harfin oluþum sayýsýný özetlemek için bir sözlük kullanan bir kod parçacýðý yazýn. 
Büyük/küçük harf dikkate almayýn, boþluklarý dikkate almayýn ve kullanýcýnýn herhangi bir noktalama iþareti girmediðini varsayalým. 
Harflerin ve sayýlarýnýn iki sütunlu bir tablosunu, harfler sýralanmýþ þekilde görüntüleyin. 
Örnek Giriþ Bu, birkaç kelimeden oluþan örnek bir metindir Bu, bazý farklý kelimelerden oluþan daha fazla örnek metindir 
Çýktý [('a', 4), (' d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), 
    ('m' , 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9) ), ('v', 1), ('w', 4), ('x', 2)]'''

def harf_sayilari(cumle):
    harf_sozlugu={}
    
    for harf in cumle :
        if harf.isalpha(): # sadece harf karakterlerini kontrol et
            harf=harf.lower() # buyuk kucuk harf farkini yok say
            harf_sozlugu[harf]=harf_sozlugu.get(harf,0)+1
    return harf_sozlugu
    
kullanicinin_cumlesi = input("lutfen bir cumle giriniz : ")
sonuc=harf_sayilari(kullanicinin_cumlesi)
print("her harfin olusum sayilari : ")

sortedList = sorted(sonuc) # []
final = {}

for i in sortedList:
    final[i] = sonuc.get(i)
final = [x for x in final.items()]
print(final)