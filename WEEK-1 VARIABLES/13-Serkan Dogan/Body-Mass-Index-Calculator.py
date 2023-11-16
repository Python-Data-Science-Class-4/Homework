# Assignment 2.3
# Body Mass Index Calculator 

# Calculate your BMI

weight = input("Enter your weight (kg);")
height = input("Enter your length (m);")

print("Your BMI is:" , float(float(weight) / float(height)**2))

if float(float(weight) / float(height)**2) >= 40:
    print("WARNING!!!\nYou are in Extremely Obesity Group !!!\nDaily exercise and less food intake are strongly recommended...")
elif 30 <= float(float(weight) / float(height)**2) < 40:
    print("You are in Obesity group...")
elif 25 <= float(float(weight) / float(height)**2) < 30:
    print("You are in Overweight group...")
elif 25 > float(float(weight) / float(height)**2) > 18.5:
    print("You are in Healthy weight group...")
else: 
    print("You are in Unhealthy Underweight group...")