sent=str(input("Please enter a sentences:"))
dic={}
for char in sent:
    if char.isalpha():
        char_low=char.lower()
        count = sent.count(char_low)
        dic[char_low] = count
        
print(dic)