##################### BMI ####################

kilo = float(input("kilonuz: "))
boy = float(input("boyunuz metre cinsinden: "))

bmi = kilo / (boy ** 2)

if bmi <= 25:
    print("kilonuz normal")
elif 25 < bmi <= 30:
    print("asiri kilolusunuz")
elif 30 < bmi <= 40:
    print("obezite")
else:
    print("asiri obezite")