class Society():
    def __init__(self, society_name=None, house_no_of_mem=None, income=None):
       self.society_name=society_name
       self.house_no_of_mem=house_no_of_mem
       self.income=income

       self.input_data()

       self.flat=self.allocate_flat()
       
    def input_data(self):
        self.society_name=input("Please enter the society name.")
        self.house_no_of_mem=input("Please enter the house number of member.")
        self.income=int(input("Please enter the your income."))
    
    def allocate_flat(self):
        if self.income < 15000:
            return 'D Type'
        elif self.income >= 15000 and self.income<20000:
            return 'C Type'
        elif self.income >= 20000 and self.income<25000:
            return 'B Type'
        else:
            return 'A Type'
    
    def show_data(self):
        return f''' 
Society Name    : {self.society_name}
Number of House : {self.house_no_of_mem}
Income          : {self.income}
Flat            : {self.flat}'''


society1 = Society()
# society2 = Society()


print(society1.show_data())


