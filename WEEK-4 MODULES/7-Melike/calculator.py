
import addition, subtraction, multiplication, division

def menu():

    function_list = [addition, subtraction, multiplication, division]
    while True:
        print("1-Addition ")
        print("2-Subtraction ")
        print("3-Multiplication ")
        print("4-Division")
        print("0-Exit the program")
        selected_action = int(input("Please select the action you want to perform.(0-4): "))

        print("\n"*30)
        if selected_action <=4 and selected_action>=1:
            a = float(input("enter the first number: "))
            b = float(input("enter the second number: "))
            function_list[selected_action-1](a,b)

            print("Current action selected")
            print("\n"*2)
        elif selected_action == 0:
            print("Logging out")
            break
        else:
            print("Please enter a number between 0 and 4 for selection")


menu()
