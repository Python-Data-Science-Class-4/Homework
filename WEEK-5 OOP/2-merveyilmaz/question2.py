class ItemInfo():
    def __init__(self, item_code, item, price, qty):
        self.item_code=item_code
        self.item=item
        self.price=price
        self.qty=qty
        self.discount=self.calculate_discount()
        self.net_price=self.buy()

    def calculate_discount(self):
        discount=0
        if self.qty<=10:
            discount=0
        elif self.qty<20 and self.qty>=11:
            discount=15
        elif self.qty>=20:
            discount=20
        return discount
    
    def buy(self):
        net_price=self.price*self.qty-self.discount
        return net_price
    
    def show_all(self):
        print(f'''
Item Code : {self.item_code}
Item      : {self.item}
Price     : {self.price}
Quantity  : {self.qty}
Discount  : {self.discount}
Net Price : {self.net_price}''')

    
item1=ItemInfo('21xyz', 'xyz', 76, 8)
item2=ItemInfo('21abc', 'abc', 43, 17)

ItemInfo.show_all(item1)
ItemInfo.show_all(item2)


