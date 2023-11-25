"""
## 5-reading_number.py
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""
def read_number(number):
    first_ten = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    differents = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

    number = int(number)

    if 10 < number < 20:
        return differents[number]
    elif number < 10:
        return first_ten[number]
    elif number % 10 == 0:
        return tens[number]
    else:
        return tens[(number // 10) * 10] + " " + first_ten[number % 10]

number = input("Enter a number:")
print(read_number(number))
