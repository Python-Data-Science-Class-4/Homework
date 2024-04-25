

#We find the numbers that are prime up to the entered number.
while True:
#To take an input from user
    entered_number =int(input("Please enter a number  :"))
    

    for number in range (2,entered_number):
            
        for i in range (2,number):
            if  number % i ==0:
                break
        else:
                print("Prime numbers up to the entered number :" ,number)
        
                    
    new_demand= str(input("Do you want to enter another number ?: Y/N "))
        
    if new_demand != "Y" and new_demand != "y":
        print("Thank you.Have a good one.")
        break

