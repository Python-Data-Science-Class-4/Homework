def shift_list(lst, n):

    # when the shift reaches the length of the list, elements returns the starting point. That's why take the modulus of shifts
    shift = n % len(lst)

    if n>=0:
        # if the number is positive go to the right
        print(lst[(len(lst) - shift):] + lst[: (len(lst)-shift)] )
    else:
        # if the number is negative go to the left
        print(lst[(shift*-1):] + lst[:(shift*-1)])

shift_list(lst=(input("Enter a comma seperated list (eg.: 1,2,3): ")).split(","), n=int(input("Enter the number of shift: ")))