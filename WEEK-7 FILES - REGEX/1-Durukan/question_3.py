## Question 3:
# Create a function that identifies and lists email addresses without domain names within a given text. 

# Example:

sample_text =  "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

# Output :
# ["franky","sinatra123"]

import re

def username_founder(text):
    pattern = re.compile(r"\S+@\S+")
    
    email_addresses = pattern.findall(text)

    return [re.split("@", i)[0] for i in email_addresses]

print(username_founder(sample_text))



