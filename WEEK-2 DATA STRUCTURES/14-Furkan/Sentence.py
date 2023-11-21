#Summarize a Sentence
# It is so good to see you again. I wish you all the best.

a = input ("Please write a sentence:")
lowercase_no_space = a.lower().replace(" ", "")
b = sorted(lowercase_no_space)

c =[]
for d in b:
    e = b. count (d)
    if (d not in c):
        print (f"{e} adet {d} bulunur.")
        c.append (d)