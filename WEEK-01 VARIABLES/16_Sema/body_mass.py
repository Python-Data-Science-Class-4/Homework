name=input("Please enter your name:")
weight=float(input("Please enter your weight:"))
height=float(input("Please enter your height:"))
result=weight / (height ** 2)
if(result<25):
    print("NORMAL")
elif(25 <= result < 30):
    print("OVERWEIGHT")
elif(30 <= result < 40):
    print("OBESE")
else:
   print("EXTREMELY OBESE") 