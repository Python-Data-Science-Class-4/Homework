'''Kullan�c�dan gelen bir c�mleyi giren ve ard�ndan her harfin olu�um say�s�n� �zetlemek i�in bir s�zl�k kullanan bir kod par�ac��� yaz�n. 
B�y�k/k���k harf dikkate almay�n, bo�luklar� dikkate almay�n ve kullan�c�n�n herhangi bir noktalama i�areti girmedi�ini varsayal�m. 
Harflerin ve say�lar�n�n iki s�tunlu bir tablosunu, harfler s�ralanm�� �ekilde g�r�nt�leyin. 
�rnek Giri� Bu, birka� kelimeden olu�an �rnek bir metindir Bu, baz� farkl� kelimelerden olu�an daha fazla �rnek metindir 
��kt� [('a', 4), (' d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), 
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