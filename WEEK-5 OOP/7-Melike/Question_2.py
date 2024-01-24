class ItemInfo():
    def __init__(self, item_code, item_name, price, quantity, discount=None):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.discount = self.calculate_discount()
        self.net_price = self.buy()
        print(self.show_all())


    def calculate_discount(self):
        if self.quantity <= 10:
            self.discount = 0
            return self.discount
        elif 11 <= self.quantity < 20:
            self.discount = 15
            return self.discount
        elif self.quantity >= 20:
            self.discount = 20
            return self.discount
    def buy(self):

       net_price = (self.price * (100 -self.discount)/100) * self.quantity # discount has been calculated as percent per item
       return net_price
    def show_all(self):
        print(f'''
ItemCode : {self.item_code}
ItemName : {self.item_name}
Price    : {self.price}
Quantity : {self.quantity}
Discount : {self.discount}
NetPrice : {self.net_price}''')


iteminfo1 = ItemInfo(1111,  "computer", 1000, 20)







