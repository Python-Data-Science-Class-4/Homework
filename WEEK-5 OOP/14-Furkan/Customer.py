class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
    def calculate_discount(self):
        total_price = self.price * self.quantity
        if total_price >= 4000:
            return 0.25 * total_price
        elif total_price >= 2000:
            return 0.15 * total_price
        else:
            return 0.10 * total_price
    def shopping_card(self, qty):
        self.quantity += qty
    def get_total_amount(self):
        return self.price * self.quantity - self.calculate_discount()
    def __str__(self):
        return f"Item: {self.name}\nPrice: {self.price} Euro\nQuantity: {self.quantity}\nTotal: {int(self.get_total_amount())} Euro"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_list = []
    def get_cust_info(self):
        return f"\nCustomer Information:\nName: {self.name}\nEmail: {self.email}"
    def __str__(self):
        for item in self.shopping_list:
            return f"{self.get_cust_info()}\n\nShopping Summary:\n{item}"

cust_name = input("Enter customer name: ")
cust_email = input("Enter customer email: ")
customer = Customer(cust_name, cust_email)

item_example = Item("Laptop", 1500)
item_example.shopping_card(3)
customer.shopping_list.extend([item_example])
print(customer)

'''Kod gayet basarili,
**get_total_amount metodunun döndürdüğü değeri int olarak döndürüyorsunuz kusuratli bir deger girildiginde hataya yol acabilir int ifadesini kaldirabiliriz.
**soruda musteri urun eklesin diyor ama siz kendiniz urun secmissiniz.'''

