text = input("Please enter your text: ").lower().replace(" ", "") # Girişi küçük harfe çevir

text = sorted(list(text))  # Metni listeye çevir, siraya diz.


letter_set=set()

summary = []

for i in text:
    if i in letter_set:
        continue
    letter_set.add(i)
    amount = text.count(i)
    letter_amount = {}
    letter_amount[f'{i}'] = amount
    summary.append(letter_amount)
    
result_list = [(key, value) for my_dict in summary for key, value in my_dict.items()]

print(result_list)
