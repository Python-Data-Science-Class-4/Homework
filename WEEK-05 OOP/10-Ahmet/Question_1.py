class Society():
    def __init__(self, society_name=None, house_no_of_mem=None, income=None):
       self.society_name=society_name
       self.house_no_of_mem=house_no_of_mem
       self.income=income

       self.input_data()

       self.flat=self.allocate_flat()
       
    def input_data(self):
        self.society_name=input("Please Enter Society Name:")
        self.house_no_of_mem=input("Please Enter House Number Of Member:")
        self.income=int(input("Please Enter Income:"))
        
              
    def allocate_flat(self):
        
        if self.income >= 25000:
            flat = "A Type"
        elif (self.income >= 20000) and (self.income < 25000):
            flat = "B Type"
        elif (self.income >= 15000) and (self.income < 20000):
            flat = "C Type"
        elif (self.income < 15000):
            flat = "D Type"
      
        return flat

      
    def show_data(self):

        return f"Society Name: {self.society_name}\nNumber of House: {self.house_no_of_mem}\nIncome: {self.income}\nFlat: {self.flat}"      


new_member = Society()

print(new_member.show_data())