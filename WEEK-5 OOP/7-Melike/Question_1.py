class Society():
    def __init__(self, society_name = "", house_no_of_mem="", income=0, flat=""):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = flat

        self.input_data()
        self.flat = self.allocate_flat()
        print(self.show_data())

    def input_data(self):
        self.society_name = input("Please enter society name : ")
        self.house_no_of_mem = input("please enter  house number: ")
        self.income = int(input("please enter income: "))

    def allocate_flat(self):

        if self.income >= 25000:
            self.flat = "A Type"
            return self.flat

        elif self.income >= 20000 and self.income < 25000:
            self.flat = "B Type"
            return self.flat

        elif self.income >= 15000 and self.income < 20000:
            self.flat = "C Type"
            return self.flat

        else:
            self.flat = "D Type"
            return self.flat


    def show_data(self):


        print(f" Society name : {self.society_name} \n Number of House : {self.house_no_of_mem} \n Income: {self.income}\n Flat: {self.flat}")






society1 = Society()

