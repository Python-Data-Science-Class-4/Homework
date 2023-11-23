first_digits = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    0:''
    }

second_digits = {
    
    2:'twenty',
    3:'thirty',
    4:'fourty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}

specials = {
    10:'ten',
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighten",
    19:"nineteen",
}

def read_number(num):
    if (num>=1 and num<=9):
        writen_num = first_digits[num]
        print(writen_num)
    elif (num>=10 and num<=19):
        writen_num = specials[num]
        print(writen_num)
    elif (num >=20 and num <=99):
        writen_num = second_digits[num//10] + " " + first_digits[num%10]
        print(writen_num)
    else:
        print('Invalid input')


read_number(int(input('Enter a number between 1-99: ')))
     