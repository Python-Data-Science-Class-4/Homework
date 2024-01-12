"""
# Question 3:
Create a function that identifies and lists email addresses without domain names within a given text. 

Example:

sample_text =  "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

Output :
["franky","sinatra123"]
"""

import re

# our match criteria is it should be seperate from the text so we need to use \b , before the @ it can be any charachter so we
# use [A-Za-z0-9._%+-]+ after @ it can follow any domain name so we use [A-Za-z0-9.-]+, but ater that we expect to see dot so we
# add \. then we need to see .com or .nl so we use [A-Z|a-z]{2,} to check of there is at least 2 letters after dot to verify email address
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_email(text):
    # we store all matching emails in a variable after finding them with regex.
    emails = re.findall(pattern, text)
    # then we apply split method to each email address  and get the first item  (username) and exlude the text after @
    names  = [email.split("@")[0] for email in emails]
    return names

user_input = input("Please write the text to find email addresses")

print(check_email(user_input))


