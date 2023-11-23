def colours(input_clr):
    
    # Join the sorted words with hyphens between them
    output_clr = '-'.join(x)

    return output_clr

# Example usage:

clr_1 = input ("Your favourite colour?: ")
clr_2 = input ("Second choice: ")
clr_3 = input ("Third choice: ")

input_clr = clr_1,clr_2,clr_3
x = sorted (input_clr)
output_clr = colours(x)

print(f'''Input   : {input_clr}
Output  : {output_clr}''')