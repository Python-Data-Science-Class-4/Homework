#After asking the user to enter their name and surname, 
#we can find the average of four different courses and the result of whether they were successful or not.
while True:

    Username=str(input("Enter name of student:"))
    Usersurname=str(input("Enter surname of student :"))

    class1_midterm = int(input("Enter your Mathematics Course Midterm Grade:"))
    class1_final = int (input("Enter your Mathematics Course Final Grade:"))
    #A formula to get the average of the course that we used every class
    avarage_class1= ((class1_midterm* 0.40 )+ (class1_final* 0.6))
    

    if avarage_class1 >= 50 :
        print(Username,Usersurname,"You passed the Math class,Your Grade :",avarage_class1)
    else:
        print("You did'nt pass the Math class ,Your Grade:",avarage_class1)

    class2_midterm = int(input("Enter your Geometry Course Midterm Grade"))
    class2_final= int(input("Enter your Geometry Course Final Grade:"))
    avarage_class2= ((class2_midterm* 0.40 )+ (class2_final* 0.6))

    if  avarage_class2 >= 50 :
        print(Username,Usersurname,"You passed the Geometry class,Your Grade :",avarage_class2)
    else:
        print("You did'nt pass the Geometry class ,Your Grade",avarage_class2)


    class3_midterm = int(input("Enter your Philosophy Course Midterm Grade:"))
    class3_final= int(input("Enter your Philosophy Course Final Grade:"))
    avarage_class3= ((class3_midterm* 0.40 )+ (class3_final* 0.6))

    if  avarage_class3 >= 50 :
        print(Username,Usersurname,"You passed the Philosophy class,Your Grade ",avarage_class3)
    else:
        print("You did'nt pass the Philosophy class ,Your Grade:",avarage_class3)

    class4_midterm = int(input("Enter your English Course Midterm Grade:"))
    class4_final = int (input("Enter your English Course Midterm Grade :"))
    avarage_class4= ((class4_midterm* 0.40 )+ (class4_final* 0.6))

    if  avarage_class4 >= 50 :
        print(Username,Usersurname,"You passed the English class,Your Grade :",avarage_class4)
    else:
        print("You did'nt pass the English class ,Your Grade:",avarage_class4)

    new_demand= str(input("Do you want to calculate for a other student ?: Y/N :"))
    
    #We are asking hier for other student
    if new_demand != "Y" and new_demand != "e":
        print("Have a nice one!")
        break
    
        




