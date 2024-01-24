#Search for eight-letter words within the text file named "eight_letter" located in the src folder and print them.

'''Import re module'''
import re 

'''Describe the text file that we want to work on it'''

eight_letter_text= "./eight_letter.txt" 

''' Read and close the file with 'with' module  '''
with open(eight_letter_text,"r") as text_file:
    read_eight_letters= text_file.read()
    
'''Create a pattern that it includes eight letters'''
pattern= (r'[A-z]{8}')

'''Find with use re module all words that has eight letters'''
result = re.findall(pattern,read_eight_letters)

print(result)
