# main.py
import sys
from math import ceil
from sum import sum
from sub import sub
from mul import mul
from div import div

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                print("Exiting... See you soon :)")
                sys.exit()

            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if choice == 1:
                result = sum(x, y)
            elif choice == 2:
                result = sub(x, y)
            elif choice == 3:
                result = mul(x, y)
            elif choice == 4:
                result = div(x, y)
                result = float(ceil(result))  # rounding up to the next integer

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

        new_calculation = input("Do you want to calculate again? (y/n): ").lower()
        if new_calculation != 'y':
            print("Exiting... See you soon :)")
            sys.exit()

calculator()
