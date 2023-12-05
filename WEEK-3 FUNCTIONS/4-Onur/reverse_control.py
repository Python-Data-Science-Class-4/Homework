def reverse_control(word):
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False

word_list = input("Please write the words you want to compare with its reverse: Ex: madam, tacocat, utrecht ")

seperated = word_list.split(",")

print_list = []
for item in seperated:
    response = reverse_control(item)
    print_list.append(response)

print(*print_list,sep=", ")