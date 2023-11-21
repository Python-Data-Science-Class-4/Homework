
# New Method For Generating Lucky Numbers

a = list (input ("Create a list of 5 numbers: "))
print (a)

x = int (input ("Enter a number: "))  
while True:    
    if x >= 0 and  x < len (a):
        new_order = a[-x:] +a[:-x]
        print(new_order)
    elif x < 0 :
        new_order = a[-x:] + a[:-x]
        print(new_order) 
    break

