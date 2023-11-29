import random
import string

n= int(input("Please enter your max-char choices for password:"))
pw=[]
def generatepass(n):
    while(len(pw)<=n-1):
        pw.append(str(random.randint(1,10)))
        pw.append(random.choice(string.ascii_lowercase))
        pw.append(random.choice(string.ascii_uppercase))
        pw.append(random.choice("!.,-_"))
        pw = pw[:n]

generatepass(n)

print("Your password:", "".join(map(str,pw)))
    


