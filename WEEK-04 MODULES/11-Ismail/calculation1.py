import division
import multiplication  #create a module to mat operation
import substruction
import addition
import sys

while True:
    try:
        request = str(input("Which math operation do you want to do?:(+,-,*,/)  ")) 
        
        if request == "+": 
            numb1 = float(input("Enter a number: "))
            numb2 = float(input("Enter a number: "))
            result_add = addition.add(numb1, numb2) #When the user enters "+"" it uses the addition module and performs the operation,then it check the errors.
            print(result_add)
        elif request == "-":
            numb1 = float(input("Enter a number: "))
            numb2 = float(input("Enter a number: "))
            result_subs = substruction.subs(numb1, numb2) ##When the user enters "-" it uses the substruction module and performs the operation,then it check the errors.
            print(result_subs)
        elif request == "*":
            numb1 = float(input("Enter a number: "))
            numb2 = float(input("Enter a number: "))
            result_mult = multiplication.mult(numb1, numb2) #When the user enters "*" it uses the multipilation module and performs the operation,then it check the errors.
            print(result_mult)
        elif request == "/":
            numb1 = float(input("Enter a number: "))
            numb2 = float(input("Enter a number: "))
            result_div = division.div(numb1, numb2) #When the user enters "/" it uses the division module and performs the operation,then it check the errors.
            print(result_div)
    
    except ValueError:
        print("Something went wrong.Please enter a valid number.") #Pass the valuerror and print
    except ZeroDivisionError:
        print("0 not divide!")#Pass the zerodivisionerror and print
    repeat_quest = input("Would you like to more calculate:(y/n)") #Ask to user for more operation
    print(repeat_quest)
    if repeat_quest.lower() == "n": #After the answer is "n" it breaks the program
        break