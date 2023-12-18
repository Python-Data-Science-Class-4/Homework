class Society():
    #Created a class as known "society", we need to take from some informations about the members.
    #firstly created normally init method, and assigned initial values 
    def __init__(self,society_name="",house_no_of_mem="",flat="",income=0) :
        self.society_name=input("Society Name:") 
        self.house_no_of_mem = int(input("Number of members:"))
        self.flat = flat
        self.income = int(input("Income :"))
        
        self.allocate_flat()
        self.show_data()
        
    def allocate_flat(self): # It assigns to which type it is based on the conditions
        if self.income >= 2500 :
            self.flat= "A Type" 
        elif 2000 <= self.income < 2500 :
            self.flat= "B type"
        elif 1500 <= self.income < 2000:
            self.flat= " C type" 
        else:
            self.flat="D type"
            
    def show_data(self):
        #it shows the data from member
        return f"Society Name: {self.society_name}\nNumber of members:{self.house_no_of_mem}\nIncome:{self.income}\nFlat Type:{self.flat}\n"
person1= Society() # created a object for example

print(person1.show_data())