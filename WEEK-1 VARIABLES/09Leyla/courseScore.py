'''
Course Score Calculation User Name, Surname, Student Number, 4 course names, 
Visa and Final grades will be required. The sum of 40% of the midterm grade and 60% of the final 
grade will give the year-end average. If the average is less than 50, "FAILED" on the screen,
50 and above, "PASSED" will be printed on the screen. This printing process is in 4 lessons. 
will be done and the lessons will be written one after the other.
'''
name=str(input("Name: "))
surname=str(input("Surname: "))
studentNumber=int(input("Student number: "))
course=0
for x in range (0,4):
 courseName=str(input("\n1. Match   2. History\n3. Biology 4. Physics\nHello " +name+ " choose your course name: "))
 if(courseName=='1'):
     matchVisa=int(input("Your visa grade for math: "))
     matchFinal=int(input("Your final grade for match: "))
     matchAverage=matchVisa*0.40 +matchFinal*0.60
     if(matchAverage<=50):
        print("You failed the exam. Your avarage:", matchAverage)
     elif(matchAverage>=50):
       print("You have passed the exam. Your avarage:", matchAverage)
     else:
        print("Something went wrong. Please try again!")

 elif(courseName=='2'):
     historyVisa=int(input("Your visa grade for history: "))
     historyFinal=int(input("Your final grade for history: "))
     historyAverage=historyVisa*0.40 +historyFinal*0.60
     if(historyAverage<=50):
        print("You failed the exam. Your avarage:", historyAverage)
     elif(historyAverage>=50):
       print("You have passed the exam. Your avarage:", historyAverage)
     else:
        print("Something went wrong. Please try again!")

 elif(courseName=='3'):
     biologyVisa=int(input("Your visa grade for biology: "))
     biologyFinal=int(input("Your final grade for biology: "))
     biologyAverage=biologyVisa*0.40 +biologyFinal*0.60
     if(biologyAverage<=50):
        print("You failed the exam. Your avarage:", biologyAverage)
     elif(biologyAverage>=50):
       print("You have passed the exam. Your avarage:", biologyAverage)
     else:
        print("Something went wrong. Please try again!")  

 elif(courseName=='4'):
     physicsVisa=int(input("Your visa grade for biology: "))
     physicsFinal=int(input("Your final grade for biology: "))
     physicsAverage=physicsVisa*0.40 +physicsFinal*0.60
     if(physicsAverage<=50):
        print("You failed the exam. Your avarage:", physicsAverage)
     elif(physicsAverage>=50):
       print("You have passed the exam. Your avarage:", physicsAverage)
     else:
        print("Something went wrong. Please try again!")           
      
















