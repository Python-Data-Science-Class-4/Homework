#product info class
class Items:
    def __init__(self, item_name, price, qty):
        self.item_name = item_name
        self.price = price
        self.qty = qty

    def calculate_discount(self):
        total_price = self.price * self.qty
        if total_price >= 4000:
            discount = 0.25
        elif total_price >= 2000:
            discount = 0.15
        else:
            discount = 0.1
        price_to_be_paid = total_price - (total_price * discount)
        return price_to_be_paid

    def __str__(self):
        return f"{self.qty} {self.item_name}(s) at ${self.price} each"

#customer info class
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = []

    def get_cust_info(self):
        return f"Customer Name: {self.name}"

    def add_to_cart(self, item):
        self.shopping_cart.append(item)

    def get_total_amount(self):
        total_amount = sum(item.calculate_discount() for item in self.shopping_cart)
        return total_amount

    def __str__(self):
        cart_items = "\n".join(str(item) for item in self.shopping_cart)
        total_amount = self.get_total_amount()
        return f"{self.get_cust_info()}\nShopping Cart:\n{cart_items}\nTotal Amount: ${total_amount:.2f}"


customer_name = input("Enter customer name: ")
customer = Customer(customer_name)

while True:
    item_name = input("Enter item name (or type 'exit' to finish): ")
    if item_name.lower() == 'exit':
        break

    item_price = float(input("Enter item price: "))
    item_qty = int(input("Enter quantity: "))
    item = Items(item_name, item_price, item_qty)
    customer.add_to_cart(item)

# Displaying customer info
print(customer)
