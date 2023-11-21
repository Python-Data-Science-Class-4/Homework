
# Unique Words

Letters_1 = sorted (input("Enter your first word: ") . lower ()) 
Letters_2 = sorted (input("Enter your second word: ") . lower ()) 

inters_letters = set(Letters_1) & set(Letters_2)  # intersection
diff_1 = set(Letters_1) - set(Letters_2)  # difference
diff_2 = set(Letters_2) - set(Letters_1)


print(f"'{inters_letters}', '{diff_1}', '{diff_2}'")