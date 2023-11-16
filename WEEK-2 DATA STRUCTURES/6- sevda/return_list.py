

list_1 = []

while True :
      i = input('Enter a number.(Once the list is complete you can press"q"):')

      if i.lower() == 'q' :
           break  
    
      list_1.append(i)
print(list_1)
while True :    

    n = int(input('Enter a number + (positive) or - (negative) :'))  # To scroll the list right / left..

      
    if n > 0 :
        list_2 = list_1[-n:] +list_1[:-n]
        print(list_2)

    elif n < 0 :
        list_2 = list_1[-n:] + list_1[:-n]
        print(list_2)


    else:
         break












