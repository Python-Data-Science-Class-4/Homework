class Society:
    def __init__(self, society_name, house_no_of_mem, flat, income):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income

    def input_data(self):
        self.society_name = input("Society name? : ")
        self.house_no_of_mem = int(input("Number of members in the house?: "))
        self.flat = ''
        self.income = float(input("The income?: "))

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = 'A Type'
        elif 20000 <= self.income < 25000:
            self.flat = 'B Type'
        elif 15000 <= self.income < 20000:
            self.flat = 'C Type'
        else:
            self.flat = 'D Type'

    def show_data(self):
        print(f"Society Name: {self.society_name}")
        print(f"House Members: {self.house_no_of_mem}")
        print(f"Income: {self.income}")
        print(f"Allocated Flat: {self.flat}")


class2 = Society("society1", 3, "B Type", 20000)

#class2.allocate_flat()

#class2.input_data()  

class2.show_data()
