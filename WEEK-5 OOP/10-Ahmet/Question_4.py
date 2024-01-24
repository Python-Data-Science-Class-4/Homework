class Customer():
    def __init__(self, factory_name, factory_type):
        self.factory_name = factory_name
        self.factory_type = factory_type
        self.get_cust_info()

    def get_cust_info(self):
        self.factory_name = input("Please Enter Factory Name:")
        self.factory_type = input("Please Enter Factory Type (A,B,C):")

class Items(Customer):
    def __init__(self, factory_name = None, factory_type = None, product = None, qty = None, price = None):
        super().__init__(factory_name, factory_type)
        self.product = product
        self.qty = qty
        self.price = price
        self.shopping_card()
        self.discount=self.calculate_discount()
        self.price_tobe_paid=self.total_amount()

    def calculate_discount(self):
        discount = 0
        total_price = 0
        total_price = Items.sum_price * Items.sum_qty
        if total_price >= 4000:
            discount = 0.25
        elif total_price >= 2000:
            discount = 0.15
        elif total_price < 2000:
            discount = 0.10
        return discount

    product_list = []
    sum_qty = 0
    sum_price = 0
    def shopping_card(self):
        
        while True:
            self.product = input("Please Enter Product Name:")
            self.qty = float(input("Please Enter Product Quantity:"))
            self.price = float(input("Please Enter Product Price:"))
            a = input("Press 'Y' if you want to finish the cart, press 'N' if you want to continue:")
            Items.product_list.append(self.product)
            Items.sum_qty += self.qty
            Items.sum_price += self.price
            if (a == "Y") or (a == "y"):
                break
    
    def total_amount(self):
        price_tobe_paid = (1-self.discount) * Items.sum_price * Items.sum_qty
        return price_tobe_paid

    
    def show_data(self):
        return f"Factory Name:{self.factory_name}\nFactory Type:{self.factory_type}\nProduct Name:{Items.product_list}\nTotal Product Quantity:{Items.sum_qty}\nTotal Product Price\n:{Items.sum_price}\nDiscount:{self.discount}\nAmount to be paid:{self.price_tobe_paid}"

items1 = Items()
print(items1.show_data())