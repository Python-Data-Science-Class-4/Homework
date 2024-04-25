"![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/e7fe133e-0e05-4f28-a43c-574f68a00cdc)"

class ItemInfo:
    __instances = []

    def __init__(self):
        self.item_code = 0 
        self.name = None
        self.price = None
        self.qty = None
        self.net_price = None
        self.discount = None
        ItemInfo.__instances.append(self.__dict__)

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty <= 20:
            self.discount = 15
        else:
            self.discount = 20
        self.net_price = (self.price * self.qty) - ((self.discount / 100) * self.price * self.qty)

    def buy(self):
        self.item_code = input("Enter item code: ")
        self.item = input("Enter item name: ")
        self.price = float(input("Enter price: "))
        self.qty = int(input("Enter quantity: "))
        self.calculate_discount()

    def show_all(self):
        print(f"Item Code: {self.item_code}")
        print(f"Item: {self.item}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.qty}")
        print(f"Discount: {self.discount}%")
        print(f"Net Price: {self.net_price}")

# Example usage
item = ItemInfo()
item.buy()
item.show_all()
