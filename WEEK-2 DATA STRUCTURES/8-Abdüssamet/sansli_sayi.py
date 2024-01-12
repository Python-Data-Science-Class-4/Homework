'''.(n) aralýðýndan þanslý sayýlarý üreten bir program yazýnýz. 
Bunlar s=[1,2,...,n] dizisinden baþlayarak üretilir. 
Ýlk geçiþte diziden her ikinci öðeyi çýkarýrýz, bu da s2 sonucunu verir. 
Ýkinci geçiþte s2 dizisinden her üçüncü elemaný çýkarýyoruz, sonuçta s3 elde ediliyor ve 
hiçbir eleman kaldýrýlamayana kadar bu þekilde ilerliyoruz. 
Ortaya çýkan dizi, elemeden sað kurtulabilecek kadar þanslý olan sayýlardýr. 
Aþaðýdaki örnek, 
n=22 Orijinal dizisi [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
2. elemanlarý çýkarýn [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
3. elemanlarý çýkarýn [1, 3, 7, 9, 13, 15, 19, 21] 
4. elementi kaldýr [1, 3, 7, 13, 15, 19] 
5. elementi kaldýr [1, 3, 7, 13, 19] 
6. element olmadýðý için her 6. elementi kaldýramýyoruz. 
Giriþ 22 Çýkýþ Þanslý sayýlar [1, 3, 7, 13, 19]
'''
N = int(input("Listenin son elemanýný giriniz: "))
list1 = []
for i in range(1, N+1):
  list1.append(i)
print(list1)
sayac = 2
while sayac <= len(list1):
  list1 = list1[::sayac]
  print(list1)
  sayac = sayac + 1