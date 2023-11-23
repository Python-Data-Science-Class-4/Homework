def alphabetical_order(words):
    words = words.split("-")
    return '-'.join(sorted(words))


test_case = alphabetical_order('green-red-yellow-black-white')
print(test_case)