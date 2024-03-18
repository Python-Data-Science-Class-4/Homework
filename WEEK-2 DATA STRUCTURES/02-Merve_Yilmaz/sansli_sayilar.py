'''
(n) aralığından şanslı sayıları üreten bir program yazın. 
Bunlar s=[1,2,...,n] dizisinden başlayarak üretilir. 
İlk geçişte diziden her ikinci öğeyi çıkarırız, bu da s2 sonucunu verir. 
İkinci geçişte s2 dizisinden her üçüncü elemanı çıkarıyoruz, sonuçta s3 elde ediliyor ve 
hiçbir eleman kaldırılamayana kadar bu şekilde ilerliyoruz. 
Ortaya çıkan dizi, elemeden sağ kurtulabilecek kadar şanslı olan sayılardır. 
Aşağıdaki örnek, n=22 
Orijinal dizisi [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
2. elemanları çıkarın [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
3. elemanları çıkarın [1, 3, 7, 9, 13, 15, 19, 21] 
4. elementi kaldır [1, 3, 7, 13, 15, 19] 
5. elementi kaldır [1, 3, 7, 13, 19] 
6. element olmadığı için her 6. elementi kaldıramıyoruz. 
Giriş 22 Çıkış Şanslı sayılar [1, 3, 7, 13, 19]
'''

sayi= int(input('Lutfen bir sayi giriniz:'))
liste=[i for i in range(1,sayi+1)]

print(liste)


for k in range(0,len(liste)):
    if k>=len(liste)-1:
        break
    del liste[k+1:len(liste):k+2]
    print('Iterasyon:', k+2,'->',liste)
      
    


    