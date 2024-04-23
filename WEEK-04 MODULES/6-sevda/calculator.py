from addition import add 
from subtraction import sub
from multipplication import multip
from division import divis
print('A calculator that performs four operations')
while True :
    try:
        answer = input("Enter for four transactions('+', '-', '*','/'),You can end the program by pressing q:")
        if  answer not in ('+', '-', '*','/','q'):
            print("please Enter for four transactions('+', '-', '*','/','q')")
            continue
        if answer.lower() == 'q' : 
            print('You logged out')
            break
    except Exception :
        print('please Enter for four transactions('+', '-', '*','/')')
    
    try :

        num1 = float(input('Enter first number:'))
        num2 = float(input('Enter second number:'))
        if answer == '+' :
           print(add(num1,num2))
        elif answer == '-' :
           print(sub(num1,num2))    
        elif answer == '*' :
           print(multip(num1,num2))
        elif answer == '/' :
           print(divis(num1,num2))
          
    except ValueError:
        print('You entered an incorrect value')
    
         
    
    