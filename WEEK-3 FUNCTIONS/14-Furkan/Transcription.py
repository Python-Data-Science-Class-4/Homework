# Write a function that outputs the transcription of an input number with two digits.
# Example:
# 28---------------->Twenty Eight

def transcription(number):
    num_0_9 =   ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_10_19 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    num_10_90 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    tens = number // 10           
    ones = number % 10              

    if tens == 0 or tens >=10:
        return ("Please, write your number in two digits.")
    elif tens == 1:
        return num_10_19[ones]
    else:
        return num_10_90[tens] + " " + num_0_9[ones]

your_number= int(input("Write a number between 10 and 99: "))
output = transcription(your_number)
print(f"{your_number} --------->",output)

''' Kod gayet guzel tebrik ederim.'''
