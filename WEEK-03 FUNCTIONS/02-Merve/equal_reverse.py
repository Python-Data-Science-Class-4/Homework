'''
Write a function that controls the given inputs whether they are equal 
to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
'''


def reverse(*kelimeler):
    # for i in kelimeler:
    #     if i==i[::-1]:
    #         print('True')
    #     else:
    #         print('False')
    print(list(map(lambda i : True if i==i[::-1] else False,kelimeler)))

reverse('madam', 'tacocat', 'utrecht')