import sys
import math
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    while True:
        print("Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            while True:
                try:
                    choice = int(input("Enter your choice (1-5): "))

                    if 1 <= choice <= 5:
                        break
                    else:
                        raise ValueError('Invalid Choice')
                except ValueError:
                    print('Invalid Choice')
            
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                sys.exit()

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            
            result = math.ceil(result)

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        again = input("Do you want to calculate again? (y/n): ").lower()
        if again == 'n':
            print("Exiting the calculator. Goodbye!")
            break


main()
