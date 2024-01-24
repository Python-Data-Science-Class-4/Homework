class ItemInfo:
    def __init__(self):
        self.item_code = 0
        self.item = None
        self.price = None
        self.qty = None
        self.discount = None
        self.net_price = None

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty <= 20:
            self.discount = 15
        else:
            self.discount = 20

        self.net_price = self.price * self.qty - (self.discount / 100 * self.price * self.qty)

    def buy(self):
        self.item_code = input("Enter item code: ")
        self.item = input("Enter item name: ")
        self.price = float(input("Enter price of each item: "))
        self.qty = int(input("Enter quantity in stock: "))
        self.calculate_discount()

    def show_all(self):
        print("\nItem Information:")
        print(f"Item Code: {self.item_code}")
        print(f"Item Name: {self.item}")
        print(f"Price: {self.price}")
        print(f"Quantity in Stock: {self.qty}")
        print(f"Discount: {self.discount}%")
        print(f"Net Price: {self.net_price}")


items = ItemInfo()
items.buy()
items.show_all()
