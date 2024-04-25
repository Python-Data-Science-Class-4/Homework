
# Write a function that takes an input of different words with hyphen (-) in between them and then:
# Sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.

def colours(input_clr):
   
    return input_clr 

# Example usage:

clr_1 = input ("Your favourite colour?: ")
clr_2 = input ("Second choice: ")
clr_3 = input ("Third choice: ")

input_clr = (clr_1, clr_2, clr_3)
output_clr = sorted (colours (input_clr)) 

print(f'''Input   : {'-'.join(input_clr)}
Output  : {'-'.join(output_clr)}''')
