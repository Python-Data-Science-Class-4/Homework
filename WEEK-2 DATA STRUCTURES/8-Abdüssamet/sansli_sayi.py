'''.(n) aral���ndan �ansl� say�lar� �reten bir program yaz�n�z. 
Bunlar s=[1,2,...,n] dizisinden ba�layarak �retilir. 
�lk ge�i�te diziden her ikinci ��eyi ��kar�r�z, bu da s2 sonucunu verir. 
�kinci ge�i�te s2 dizisinden her ���nc� eleman� ��kar�yoruz, sonu�ta s3 elde ediliyor ve 
hi�bir eleman kald�r�lamayana kadar bu �ekilde ilerliyoruz. 
Ortaya ��kan dizi, elemeden sa� kurtulabilecek kadar �ansl� olan say�lard�r. 
A�a��daki �rnek, 
n=22 Orijinal dizisi [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
2. elemanlar� ��kar�n [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
3. elemanlar� ��kar�n [1, 3, 7, 9, 13, 15, 19, 21] 
4. elementi kald�r [1, 3, 7, 13, 15, 19] 
5. elementi kald�r [1, 3, 7, 13, 19] 
6. element olmad��� i�in her 6. elementi kald�ram�yoruz. 
Giri� 22 ��k�� �ansl� say�lar [1, 3, 7, 13, 19]
'''
N = int(input("Listenin son eleman�n� giriniz: "))
list1 = []
for i in range(1, N+1):
  list1.append(i)
print(list1)
sayac = 2
while sayac <= len(list1):
  list1 = list1[::sayac]
  print(list1)
  sayac = sayac + 1