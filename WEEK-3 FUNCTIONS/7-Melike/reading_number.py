#################### 5- reading_number #####################

def reading_number(x):
    first = [ " ", "one", "two", "three", "four", "five", "six", 'seven', "eight", "nine"]
    second = [" ", "ten", "twenty", "thirty", "forty", "fifty", "sixty", 'seventy', "eighty", "ninety"]
    order = ["",  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"] # numbers 11 to 20


    one1 = x%10 # ones digit of the number
    ten10 = x//10 # tens digit of the number
    if ten10 == 1 and one1 == x%10 :
        print(order[one1])
    else:
        print(second[ten10], first[one1])

number = int(input("enter a number :"))
reading_number(number)