name=str(input("Please enter a name: "))
new_name=name[::-1]
if (name.upper()==new_name.upper()):
    print(new_name, " is an equal reverse word")
else:
    print(new_name, " is not an equal reverse word")