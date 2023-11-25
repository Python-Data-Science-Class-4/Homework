def num_text(num):

    number_dict = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }

    if num in number_dict:
        text_num = number_dict[num]
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        text_num = number_dict[tens_digit * 10]
        if ones_digit > 0:
            text_num += ' ' + number_dict[ones_digit]

    return text_num

input_number = int(input("Please enter a two digit number:  "))
result = num_text(input_number)

print(f"{input_number} ----------------> {result}")
