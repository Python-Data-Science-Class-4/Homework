'''Giri� olarak iki kelime alan ve �� ��eyi i�eren bir listeyi a�a��daki s�raya g�re d�nd�ren bir program yaz�n: 
�ki kelime aras�ndaki payla��lan harfler. 
1. kelimeye �zel harfler. 
2. kelimeye �zel harfler. 
��kt�n�n her eleman� benzersiz harflere sahip olmal� ve alfabetik olarak s�ralanmal�d�r. 
 Ayarlanm�� i�lemleri kullan�n. Dizeler her zaman k���k harf olacak ve herhangi bir noktalama i�areti i�ermeyecektir. 
�rnek Giri�1 keskin Giri�2 sabun ��k�� ['aps', 'hr', 'o']'''

#a b c � d e f g � h i � j k l m n o � p r s � t u � v y z
#A B C � D E F G � H � I J K L M N O � P R S � T U � V Y Z
alfabe=("ABC�DEFG�H�IJKLMNO�PRS�TU�VYZabc�defg�hi�jklmno�prs�tu�vyz")
print(alfabe)

kelime1=input("l�tfen birinci kelimeyi giriniz : ")
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