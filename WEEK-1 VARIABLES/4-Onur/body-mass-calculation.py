weight = float(input("Your weight?"))
height = float(input("Your height in cm. Example: 170?"))/100

body_mass  = weight/(height*height)
print(f"Your BMI is = {body_mass:.2f}")

if body_mass < 25:
    print("NORMAL")
elif 25 <= body_mass <30:
    print("OVER WEIGHT")
elif 30 <= body_mass <40:
    print("OBESE")
else:
    print("EXTREMELY OBESE")