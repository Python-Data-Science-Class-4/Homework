'''Ýki girdi alan bir program yazýn; 
biri liste diðeri sayý olup, n pozitif (negatif) olduðunda listedeki elemanlarýn n basamak saða (sola) kaydýrýlmasýyla elde edilen listeyi döndürür. 
Bir öðe listenin sonunun ötesine kaydýrýlýrsa sarmalamayý kullanýn, ardýndan listenin baþýndan baþlayarak kaydýrmaya devam edin. 
Örnek Giriþler [1, 2, 3, 4, 5], 2 Çýkýþ [4, 5, 1, 2, 3] Giriþler [1, 2, 3, 4, 5], -2 Çýkýþ [3, 4, 5, 1, 2]'''

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
        
        