import sys
import math
from add import add_
from subt import subt_
from multiply import mult_ 
from division import div_

def user_choice():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    return choice

def again():
    return input("Do you want to calculate again? (y/n): ").lower() == 'y'

def calc():
    while True:
        try:
            choice = user_choice()
            if choice == '5':
                print("Goodbye!")
                sys.exit()

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = 0
            if choice == '1':
                result = math.ceil(add_(num1, num2))
            elif choice == '2':
                result = math.ceil(subt_(num1, num2))
            elif choice == '3':
                result = math.ceil(mult_(num1, num2))
            elif choice == '4':
                result = math.ceil(div_(num1, num2))
            
            print(f"Result: {result}")

        except ValueError:
            print("Please enter a number between 1-5.")
            continue
        except ZeroDivisionError:
            print("Not divide by zero")

        if not again():
            print("Goodbye!")
            break

calc()