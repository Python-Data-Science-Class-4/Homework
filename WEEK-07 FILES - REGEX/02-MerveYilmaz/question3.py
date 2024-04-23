'''
Create a function that identifies and lists email addresses without domain names within 
a given text.

Example:

sample_text = "The advencements in biomarine studies franky@google.com with the investments 
necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

Output : ["franky","sinatra123"]
'''

import re
def without_domain(data):
    pattern= re.compile(r"\w*\@")
    result=re.findall(pattern, data)
    list=[]
    for i in result:
        i=re.split('@',i)[0]
        list.append(i)
    return list

text='''The advencements in biomarine studies franky@google.com with the investments 
necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'''

print(without_domain(text))

