
############# Homework 2 ###########

elements = list(input("enter objects: "))
list1 = []
for i in elements:
    list1.append(int(i))
print(list1)

number = int(input("please enter a number: "))
def rotate(nums, k): # I found this function op internet #
    k %= len(nums)
    nums[:] = nums[-k:] +nums[:-k]


rotate(list1, number)
print(list1)