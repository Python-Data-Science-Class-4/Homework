# Common features of words
 
word1 = input('Enter the 1st word:')
word2 = input('Enter the 2nd word:')
A = set(word1.lower())
B = set(word2.lower())

difference_1 = list(A.difference(B))
C = sorted(difference_1)
difference_2 = list(B.difference(A))
D = sorted(difference_2)
symmetric = list(A.symmetric_difference(B))
E = sorted(symmetric)

print([(''.join(C)),(''.join(D)),(''.join(E))])
