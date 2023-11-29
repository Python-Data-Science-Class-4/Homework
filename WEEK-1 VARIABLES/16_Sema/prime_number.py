def prime_number(number):
    num=int(number)
    if(num<=1):
        print("Your number ", num, "is not a prime number")
    else:
        result=True
        for a in range(2, num):
            if((num%a)==0):
               result=False 
               break
            else:
                result=True
        if(result):
          print("Your number ", num, "is a prime number")  
        else:
          print("Your number ", num, "is not a prime number")            


number=input("Please enter a number")
prime_number(number)