def sort_input(words):
    unordered_list = words.split("-")
    unordered_list.sort()
    return "-".join(unordered_list)

words = input("Please write the words you want to sort. Ex:green-red-yellow-black-white")

print(sort_input(words))