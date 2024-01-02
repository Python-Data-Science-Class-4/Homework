'''Question 3:
Create a function that identifies and lists email addresses without domain names within a given text.

Example:

sample_text = "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

Output : ["franky","sinatra123"]'''

import re

def find_usernames_without_domain(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            # Define a regular expression pattern for finding email addresses
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            # Find all email addresses in the text
            email_matches = re.findall(email_pattern, text)
            print("Emails found: \n" , email_matches)

            # Extract the local part (username) without the domain for each email
            usernames_without_domain = [re.split('@', email)[0] for email in email_matches]

            return usernames_without_domain

    except FileNotFoundError:
        print(f"\nFile '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'WEEK-7 FILES - REGEX/3-Yusuf/src/Eight_letter.txt'
output = find_usernames_without_domain(file_path)
print("\nusernames without domains: \n", output)
