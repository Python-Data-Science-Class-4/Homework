'''
İki girdi alan bir program yazın; biri liste diğeri sayı olup, 
n pozitif (negatif) olduğunda listedeki elemanların n basamak sağa (sola) 
kaydırılmasıyla elde edilen listeyi döndürür. 
Bir öğe listenin sonunun ötesine kaydırılırsa sarmalamayı kullanın, 
ardından listenin başından başlayarak kaydırmaya devam edin. 
Örnek 
Girişler [1, 2, 3, 4, 5], 2 Çıkış [4, 5, 1, 2, 3] 
Girişler [1, 2, 3, 4, 5], -2 Çıkış [3, 4, 5, 1, 2]
'''

sayi_liste=int(input('Liste uretmek icin bir sayi giriniz:'))
sayi=int(input('Liste elemanlarini kaydirmak icin bir sayi giriniz:'))

liste=[i for i in range(1, sayi_liste+1)]
print('Liste:',liste)

if sayi>=sayi_liste:
    kalan=sayi%sayi_liste
    liste_n=liste[-kalan:]+liste[0:-kalan]
    print('Cikti:',liste_n)
else:
    liste_n=liste[-sayi:]+liste[0:-sayi]
    print('Cikti:',liste_n)