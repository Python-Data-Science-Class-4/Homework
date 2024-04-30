class ItemInfo():
    def __init__(self, item, item_code=0, price="", qty="", net_price="", discount=""):
        self.item = item
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.net_price = net_price
        self.discount = discount

        self.buy()
        self.calculate_discount()
        self.show_all()
        
    def buy(self):
        self.item_code = input("Please enter your item code: ")
        self.item = input("Please enter the item name: ")
        self.price = float(input('Please enter the price of item:'))
        self.qty = int(input("Please enter the quantity of item: "))

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 15
        else:
            self.discount = 20

        self.net_price = (self.price*((100-self.discount)/100))*self.qty

    def show_all(self):
         print(f'''
Item Code          :{self.item_code}
Item Name          :{self.item}
Price of each      :{self.price}               
Quantity in Stock  :{self.qty} 
Discount           :{self.discount}
Net Price          :{self.net_price}
''')
         


item1 = ItemInfo('cikolata')

''' Gayet basarili tebrik ederim.'''
