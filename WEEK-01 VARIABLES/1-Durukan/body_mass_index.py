weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height**2)

if bmi < 25:
    print(f"Your body mass index {bmi} is NORMAL")
elif 25 <= bmi <= 30:
    print(f"Your body mass index {bmi} is OVER-WEIGHT")
elif 30 < bmi < 40:
    print(f"Your body mass index {bmi} is EXTREMELY-OBSE")
elif bmi <= 40:
    print(f"Your body mass index {bmi} is WARNING")