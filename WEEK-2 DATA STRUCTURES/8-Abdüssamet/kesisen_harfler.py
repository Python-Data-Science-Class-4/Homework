'''Giriþ olarak iki kelime alan ve üç öðeyi içeren bir listeyi aþaðýdaki sýraya göre döndüren bir program yazýn: 
Ýki kelime arasýndaki paylaþýlan harfler. 
1. kelimeye özel harfler. 
2. kelimeye özel harfler. 
Çýktýnýn her elemaný benzersiz harflere sahip olmalý ve alfabetik olarak sýralanmalýdýr. 
 Ayarlanmýþ iþlemleri kullanýn. Dizeler her zaman küçük harf olacak ve herhangi bir noktalama iþareti içermeyecektir. 
Örnek Giriþ1 keskin Giriþ2 sabun Çýkýþ ['aps', 'hr', 'o']'''

#a b c ç d e f g ð h i ý j k l m n o ö p r s þ t u ü v y z
#A B C Ç D E F G Ð H Ý I J K L M N O Ö P R S Þ T U Ü V Y Z
alfabe=("ABCÇDEFGÐHÝIJKLMNOÖPRSÞTUÜVYZabcçdefgðhiýjklmnoöprsþtuüvyz")
print(alfabe)

kelime1=input("lütfen birinci kelimeyi giriniz : ")
kelime2=input("lutfen ikinci kelimeyi  giriniz : ")

kelime1=kelime1.lower()
kelime2=kelime2.lower()

kelime1=set(kelime1)
kelime2=set(kelime2)



ortakharf=kelime1&kelime2
ortakharf=list(ortakharf)
ortakharf.sort()
print('iki kelimenin ortak harfleri :',ortakharf)

fark1=kelime1-kelime2
fark1=list(fark1)
fark1.sort()
print('1.kelimenin ozel harfleri :',fark1)

fark2=kelime2-kelime1
fark2=list(fark2)
fark2.sort()
print('2.kelimenin ozel harfleri :',fark2)



ortakharf = [harf for harf in ortakharf if harf in alfabe]
fark1 = [harf for harf in fark1 if harf in alfabe]
fark2 = [harf for harf in fark2 if harf in alfabe]

sonuc=[]
sonuc.append(str.join('', ortakharf))
sonuc.append(str.join('', fark1))
sonuc.append(str.join('', fark2))

'''for i in alfabe:
    sonuc.append(i)

    
'''
print(sonuc)