

list_1 = []

while True :
      i = input('Enter a number.(Once the list is complete you can press"q"):')

      if i.lower() == 'q' :
           break  
    
      list_1.append(i)
print(list_1)
while True :    

    n = int(input('Enter a number + (positive) or - (negative)To rotate the list right or left :')) 
     # To scroll the list right / left..

    n %= len(list_1)

    list_2 = list_1[-n:] + list_1[:-n]
    print(list_2)


'''Kod istwnileni veriyor ama liste uzunlugundan  buyuk bir sayi girdigimde hicbir degisiklik yapmiyor. Mod kullanarak islem yapmasi gerekiyor.
 n %= len(list_1)

    list_2 = list_1[-n:] + list_1[:-n]
    print(list_2)
    
'''











