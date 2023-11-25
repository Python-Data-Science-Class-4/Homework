"""
## 5-reading_number.py
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""
def read_number(sayı):
    
    
    first_ten={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    
    tens={10:"ten",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    
    differents={11:"eleven",12:"twelwe",13:"thirteen",14:"fourteen",15:"fiveteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    if 10 < sayı < 20:
        return differents[sayı]
    elif sayı < 10 :
        return first_ten[sayı]
    
    tensdigit= sayı // 10
    
    one_digit = sayı % 10
    
    if one_digit==0:
        return tens[tensdigit]
    
    else:
        return tens[tensdigit] + first_ten[one_digit]
    
    
    
sayı= input("Enter a number:")

print(read_number(sayı))