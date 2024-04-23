

'''
## 2 - Calculator

As a user, I want to use a program which can calculate basic mathematical operations with using functions. So that I can add, subtract, multiply or divide my inputs. 
The code must always works until the user want to exit. The code should never crash: while receiving information from the user, calculating, etc.

## Acceptance Criteria:
-  The calculator must support the Addition, Subtraction, Multiplication and Division operations. 
-  Define four modules in four different files for each of them, with two float numbers as parameters. 
-  And you must import these modules into your main file. To calculate the result, use math.ceil() and get the next integer value greater than the result. 
-  Create a menu using the print command with the respective options and take an input choice from the user. 
-  Use if/elif statements for cases and call the appropriate functions. 
-  Use try/except blocks in main file and modules to prevent crashes. 
-  Ask user if it wants to calculate again. To implement this, take the input from user y(yes) or n(no). 
-  (use import sys, ceil and other calculation functions from the math module)
'''

import sys
from addition import addition
from subtraction import subtract
from multiplication import multiply
from division import divide

# we need to continue the operation until user cancels so while is more appropriate
while True:
    # we display each option to user for selection
    print("Welcome to the Calculator! Choose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    # we use try except inside while to catch all exceptions so program will not stop when user does not provide correct input
    try:
        choice = input("Enter choice Ex:2: ")

        #when user selects 5 we exit the program with sys.exit to initiate healhty exit
        if choice == '5':
            sys.exit()

        #no matter what user selects(except 5) we will ask 2 numbers to make an operation
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # we check request and call correct function
        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input")

        # we ask if the user wants to calculate again
        again = input("Do you want to calculate again? (y/n): ")

        # we make the input lowercase and check if that is yes so we can break, otherwise while loop will continue
        if again.lower() != 'y':
            break

    except Exception as e:
        print("An error occurred:", e)

print("Program exited.")