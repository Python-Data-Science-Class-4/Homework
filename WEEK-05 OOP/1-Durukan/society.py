class Society():
    def __init__(self):
        # Start these functions when Society class called.
        self.input_data()
        self.allocate_flat()
        print(self.show_data())

    def input_data(self):
        # Take the inputs and assign them to the variables of created object with self parameter.
        self.society_name = input('Enter your society name: ')
        self.house_no_of_mem = input('Enter the house number of member: ')
        while True:
            try:
                self.income = int(input('Please enter your income: '))
                break 
            except ValueError:
                print("Invalid input. Income should be an integer")


    def allocate_flat(self):
        # According to the income value of created object assign a flat with if-elif-else block
        if self.income < 15000:
            self.flat = "D Type"
        elif self.income >= 15000 and self.income<20000:
            self.flat = 'C Type'
        elif self.income >= 20000 and self.income<25000:
            self.flat = 'B Type'
        else:
            self.flat = 'A Type'

    
    def show_data(self):
        # Returns the values of variables to display the values.
        return f'''
Society Name    : {self.society_name}
Number of House : {self.house_no_of_mem}
Income          : {self.income}
Flat            : {self.flat}'''


society = Society()

'''Çok güzel ellerinize sağlık'''
