'''rite a program that takes two inputs; one of them is a list and the other is a number,
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative).
Use wrap-around if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.
Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]'''


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











