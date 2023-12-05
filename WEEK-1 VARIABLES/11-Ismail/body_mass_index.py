#Body Mass Index Calculator Parameter showing whether a person's weight is normal for their height. 
#It is called Body Mass Index. In short, a person's weight is equal to a person's height. If we divide it by its square,
# the body mass index is obtained. 
#User's weight and height If the result by taking the length is below 25, NORMAL, if it is between 25-30 OVER WEIGHT,
#OBSE if 30-40, EXTREMELY OBSE if 40 and over print a warning.




while True:
    #We created a variable called -persons_weight- to allow the user to enter their weight.
    persons_weight=float(input("Please enter your weight in kg:"))
    #We created a variable called -persons_height- to allow the user to enter their height.
    persons_height=float(input("Please enter your height in cm:"))

    body_mass_index = (persons_weight/((persons_height**2)/100))

    if body_mass_index <= 0.25:
        print(body_mass_index,":Normal")
    elif 0.25 < body_mass_index >=0.30:
        print(body_mass_index, ":Over Weight")
    elif 0.30 < body_mass_index >= 0.40:
        print(body_mass_index,":Obse") 
    elif 0.40 < body_mass_index :
        print (body_mass_index,":Extremly Obse")
    else:
        print("Something went wrong?!")
        
    break        