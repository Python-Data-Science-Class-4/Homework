'''
Body Mass Index Calculator Parameter showing whether a person's weight is normal for their height. 
It is called Body Mass Index. In short, a person's weight is equal to a person's height. 
If we divide it by its square, the body mass index is obtained. 
User's weight and height 
If the result by taking the length is below 25, NORMAL, 
if it is between 25-30 OVER WEIGHT, OBSE if 30-40, EXTREMELY OBSE if 40 and over print a warning.
'''

while True:
    weight=float(input("Enter your weight: "))
    height=float(input("Enter your height: "))
    bodyMass= weight/height*height      #kg/m2
    if(bodyMass<=25):
        print("NORMAL")
    elif(25<=bodyMass<=30):
        print("OVER WEIGHT")  
    elif(30<=bodyMass<=40):
        print("EXTREMELY OBSE")    
    elif(bodyMass>=40):
        print("Warning, please consult with a doctor")    
            
#I can check that the input is not a string
