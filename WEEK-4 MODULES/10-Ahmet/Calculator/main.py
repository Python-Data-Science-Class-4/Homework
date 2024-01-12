"""A program that can calculate basic mathematical operations using functions.

- The calculator supports Addition, Subtraction, Multiplication and Division.
- It uses four different modules for four different operations.
- Uses math.ceil() to calculate the result and retrieves the next integer value greater than the result.
- The operation to be performed is selected via the menu.
- Uses try/except blocks to avoid crashes.
- Asks the user if they want to recalculate."""




import addition
import subtraction
import multiplication
import division

loop = True

while loop:

    loop = False

    print("""
            *** CALCULATOR ***
      
      Please Select the Transaction You Want to Perform.

      1- Addition
      2- Subtraction
      3- Multiplication
      4- Division
      :
      """)
    
    #The mathematical operation to be performed should be selected as "1,2,3,4".

    selection = (input())


    # Addition
    
    if(selection == '1'):
        while True:
            try:
                x = float(input("Enter the First Number:"))     #If the correct type of value is entered, the condition is true.
                break
            except:
                print("please enter a number")      #If the wrong data type is entered, the user is warned to enter the correct data type.

        while True:
            try:
                y = float(input("Enter the Second Number:"))
                break
            except:
                print("please enter a number")
        result = addition.calculation(x,y)  #To perform the addition, the "calculation" function is called from the "addition" module 
                                            #and the "x" and "y" values we receive from the user are assigned as parameters.
    # Subtraction
    
    elif(selection == '2'):
        while True:
            try:
                x = float(input("Enter the First Number:"))
                break
            except:
                print("please enter a number")

        while True:
            try:
                y = float(input("Enter the Second Number:"))
                break
            except:
                print("please enter a number")
        result = subtraction.calculation(x,y)

    # Multiplication

    elif(selection == '3'):
        while True:
            try:
                x = float(input("Enter the First Number:"))
                break
            except:
                print("please enter a number")
        while True:
            try:
                y = float(input("Enter the Second Number:"))
                break
            except:
                print("please enter a number")
        result = multiplication.calculation(x,y)

    # Division

    elif(selection == '4'):
        while True:
            try:
                x = float(input("Enter the First Number:"))
                break
            except:
                print("please enter a number")
        while True:
            try:
                y = float(input("Enter the Second Number:"))
                break
            except:
                print("please enter a number")
        result = division.calculation(x,y)
    else:
        print("Please Make a Valid Selection") 
        loop = True
        continue
    

    print(f"Conclusion: {result}")

    i = True


    # The user is asked if he/she wants to take any further action.
    
    while i:
        i = False

        a = input("Would You Like to Take Any Other Transaction? (Y/N)")

        if (a == 'y') or (a == 'Y'):
            loop = True
        elif (a == 'n') or (a == 'N'):
            print("Good Bye")
        else:
            print("Please Make a Valid Selection (Y/N):")
            i = True