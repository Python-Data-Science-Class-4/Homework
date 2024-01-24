class ItemInfo:
    def __init__(self, item_code=0, item_name='', price_of_each_team=0, quantity_in_stock=0,
                 discount_percentage_on_the_item=0, price_after_discount=0):
        self.code = item_code
        self.item = item_name
        self.price = price_of_each_team
        self.qty = quantity_in_stock
        self.discount = discount_percentage_on_the_item
        self.net_price = price_after_discount

    def calculate_discount(self):
        if self.qty<=10:
            self.discount = 0
        elif 11<=self.qty<=20:
            self.discount = 15
        elif self.qty>=20:
            self.discount = 20
        self.net_price = (self.price * self.qty) - self.discount  

    def buy(self):
        self.code = input("Enter item code: ")
        self.item = input("Enter the name of item: ")
        self.price = int(input("Enter the price: "))
        self.qty = int(input("Enter the quantity in stock: "))   
        self.calculate_discount()   
    
    def show_all(self):
        print(f'''
        Item Code : {self.code}
        Item Name : {self.item}
        Price     : {self.price}
        Quantity  : {self.qty}
        Discount  : {self.discount}
        Net Price : {self.net_price}''')

Info = ItemInfo()
Info.buy ()
Info.show_all ()
''' Kod gayet basarili calisiyor.
**show_all fonksiyonunun çıktısını düzenlemek için f-string kullanabilirsiniz.
**calculate_discount fonksiyonunu buy fonksiyonu içinde çağırmadan önce doğrudan __init__ içinde çağırabilirsiniz.'''
        

    
