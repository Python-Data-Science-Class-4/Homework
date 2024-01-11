"![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/f72b1724-3391-4682-81ba-f6abc5b46b67)"

class Society:
    __instances = []

    def __init__(self, name, house_no, flat, income):
        self.society_name = name
        self.house_no_of_mem = house_no
        self.income = income
        self.flat = self.__allocate_flat(self.income)
        
        Society.__instances.append(self)

    # method to read the data about an instance
    def input_data(self):
        return f"Society Name: {self.society_name}\nHouse No of Members: {self.house_no_of_mem}\nFlat: {self.flat}\nIncome: {self.income}"

    # we define private method to allocate flat category for each instance
    def __allocate_flat(income):
        if income >= 25000:
            return "A Type"
        elif income >= 20000:
            return "B Type"
        elif income >= 15000:
            return "C Type"
        else:
            return "D Type"
        
    # since we want information about class, we need to define this as class method
    # we use the method we define to show each instance information 
    @classmethod
    def show_data(cls):
        for instance in cls.__instances:
            print(instance.input_data())

# Example usage
s1 = Society("Green Park", 101, "A Type", 30000)
s2 = Society("Blue Ridge", 102, "B Type", 21000)

print(s1.show_data())
Society.show_data()