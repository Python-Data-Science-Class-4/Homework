'''�ki girdi alan bir program yaz�n; 
biri liste di�eri say� olup, n pozitif (negatif) oldu�unda listedeki elemanlar�n n basamak sa�a (sola) kayd�r�lmas�yla elde edilen listeyi d�nd�r�r. 
Bir ��e listenin sonunun �tesine kayd�r�l�rsa sarmalamay� kullan�n, ard�ndan listenin ba��ndan ba�layarak kayd�rmaya devam edin. 
�rnek Giri�ler [1, 2, 3, 4, 5], 2 ��k�� [4, 5, 1, 2, 3] Giri�ler [1, 2, 3, 4, 5], -2 ��k�� [3, 4, 5, 1, 2]'''

list1=[]
sayilar=input('lutfen koseli parantez ile dilediginiz kadar sayi giriniz')
num=int(input('lutfen bir saayi giriniz'))

for i in sayilar:
    list1.append(i)

'''if num<0 :
    for i in range(num, 0) :
        removed_element = list1.pop(0)
        list1.append(removed_element)
else :    
    for i in range(0, num):
        removed_element = list1.pop(-1)
        list1.insert(0, removed_element)'''


list2 = []
for i in list1:
    list2.append(i) 

for index in range(len(list1)):
    list2[(index + num) % len(list1)] = list1[index]
    
print(list2)
        
        