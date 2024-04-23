####################################
import re
def find_email():
    text = input("enter your text:")
    split_term = r'(\S+)(@\S+)'
    split_list = re.findall(split_term,text)



    for i in split_list:
        print(i[0])


find_email()

sample_text = "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."
