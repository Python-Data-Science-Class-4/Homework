'''
Create a function that identifies and lists email addresses without domain names within a given text.

Example:

sample_text = "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

Output : ["franky","sinatra123"]  '''


'''Import re module'''
import re 

def without_domain(text=None):
    
    '''Created a pattern and use re module that helps to find domains'''
    pattern= (r'\w+@\w+\.\w+')
    
    matches=re.findall(pattern, text)
    
    
    
    if len(matches)== 0 :
        
        return "There is no email adress here!"
    
    else:
        '''Now, we have a array from re module, we will work on array'''
        without_domain = []
        
        for match in matches : 
            '''This loop splits the domain names before the '@' sign and adds the list at above '''
            without_domain.append(match.split("@")[0])
            
    return without_domain

        
    
try2=" The advencements in biomarine studies franky@google.com , 5_username34_@gmail.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms"

output = without_domain(try2)
print(output)