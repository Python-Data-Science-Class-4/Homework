number = int(input("Please write an integer to find its lucky numbers. Ex:22"))

#Generate a list until the specified number
initial_list = list(range(1,number+1))

#Define a variable to calculate steps and hold the value
step = 2
print(f"""Initial list 
      {initial_list}
      Calculating the lucky numbers... """)

#Define a loop to check if the step exceeds the lenght of the list or not
while step<=len(initial_list):
    #Apply a function to every item of the list, in order to apply "%"to check of the nth item is reached and discard that
    #we need to shift the index of the list to left and start from 1. lets call this dummy_index, but this is only to % calculation. so we need to create 
    # we need to calculate the % based on dummy_index but we need to get the value from actual index so we use initial_list[x-1]
    lucky_list = [ initial_list[x-1] for x in range(1,len(initial_list)+1) if x % step != 0]
    print(f"""After step = {step} is 
          {lucky_list}""")   
    
    #We need to update our initial list so we can move to next step
    initial_list = lucky_list
    
    #increase the step until the list length is reached
    step += 1


