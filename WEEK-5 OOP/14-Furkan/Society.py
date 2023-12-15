class Society:
    def __init__(self, society_name ="", house_no_of_mem="", flat="", income=0):
        self.society = society_name
        self.house = house_no_of_mem
        self.flat = flat
        self.income = income
    def input_data(self):
        self.society = input("Enter society name: ")
        self.house = input("Enter house number: ")
        self.income = int(input("Enter income: "))
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        elif 20000 <= self.income < 25000:
            self.flat = "B Type"
        elif 15000 <= self.income < 20000:
            self.flat = "C Type"
        else:
            self.flat = "D Type"
    def show_data(self):
        print(f"Society: {self.society}")
        print(f"House number: {self.house}")
        print(f"Income: {self.income} Euro")
        print(f"Flat: {self.flat}")
members = Society()
members.input_data()
members.allocate_flat()
members.show_data()

''' Kod gayet basarili tebrik ederim. 
**show_data fonksiyonunun print yerine return kullanirsaniz daha esnek olabilir.'''
