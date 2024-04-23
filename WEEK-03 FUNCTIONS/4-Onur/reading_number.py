"""
## 5-reading_number.py
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""

def number_to_words(number):
    #for each digit in the number we keep a dictionary of how to spell

    zero_nine = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    tens = {1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

    # for numbers 11 to 19 we keep a seperate because they are outliers
    special = {11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
             15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

    # check if the number is outlier
    if 10 < number < 20:
        return special[number]

    # find the each digit for tens and ones - in turkish onlar basamagi ve birler basamagi
    tens_digit = number // 10
    ones_digit = number % 10

    #return the string
    if ones_digit == 0:
        return tens[tens_digit]
    else:
        return tens[tens_digit] + " " + zero_nine[ones_digit]

number = int(input("Please write an integer number between 10-99 to find its transcription"))

print(f"{number}----------------> {number_to_words(number)}")
