# Write a function that outputs the transcription of an input number with two digits.
#Example:
#28---------------->Twenty Eight

def reading_numbers(number):
    '''This functions prints the transcript of an entered two-digit number.'''
    digits_number = [int(digit) for digit in str(number)]
    ones_place = {0:'',1:'one', 2:'two',3 :'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine' }
    ten_place = {1:'teen',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    other_numbers = {10:'ten',11:'eleven',12 :'twelve',13:'thirteen',15:'fifteen'}
    if  10<= number < 14  or number == 15:
        print(number,'--------->',other_numbers[number] ) 
    if  15 < number < 20  or number == 14 :
        print (number, '---------->' ,ones_place[digits_number[1]],ten_place[digits_number[0]],sep='')
    if 100 > number > 19 :
        print(number, '---------->' ,ten_place[digits_number[0]],ones_place[digits_number[1]])    

reading_numbers(34)


