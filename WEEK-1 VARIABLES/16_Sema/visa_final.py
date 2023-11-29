
for a in range(4):
    name=input("Enter your name: ")
    surname=input("Enter your surname: ")
    visa=float(input("Enter your visa: "))
    final=float(input("Enter your final: "))
    result=(visa*0.4)+(final*0.6)
    if result>=50:
        print("Passed")
    else:
        print("Failed")