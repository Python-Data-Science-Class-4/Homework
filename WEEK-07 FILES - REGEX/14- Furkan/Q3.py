
# Create a function that identifies and lists email addresses without domain names within a given text.

import re

def find_emails(text):
   
    pattern = re.compile(r'\b([\w.]+)@[\w.]+\b')
    matches = pattern.findall(text)

    # Extract the local parts of the email addresses
    local_parts = [match.split('@')[0] for match in matches]

    return local_parts

# Example:
sample_text = '''The advancements in biomarine studies franky@google.com with the investments necessary 
                and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'''

output = find_emails(sample_text)
print(output)
