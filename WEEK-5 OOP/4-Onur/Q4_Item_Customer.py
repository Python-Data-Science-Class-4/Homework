"![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/114c227a-5cca-496c-92ce-4714c04eb4fa)"

class Items:
    def __init__(self):
        self.cart = []
        self.total_price = 0

    def add_to_cart(self, item, price, qty):
        self.cart.append((item, price, qty)) #add items to cart and calculate total price
        self.total_price += price * qty

    # discount method
    def calculate_discount(self):
        if self.total_price >= 4000:
            return 0.25 * self.total_price
        elif self.total_price >= 2000:
            return 0.15 * self.total_price
        else:
            return 0.10 * self.total_price

    # clculate the price to pay
    def get_total_amount(self):
        return self.total_price - self.calculate_discount()

    # add every line to string to have one string to print
    def __str__(self):
        cart_str = "Shopping Cart:\n"
        for item, price, qty in self.cart:
            cart_str += f"Item: {item}, Price: {price}, Quantity: {qty}\n"
        cart_str += f"Total Price: {self.total_price}\n"
        cart_str += f"Total Price after Discount: {self.get_total_amount()}\n"
        return cart_str

    #example data generation
    def shopping_cart(self):
        self.add_to_cart('Item1', 1000, 3) 
        self.add_to_cart('Item2', 500, 2)

class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.shopping_cart = Items()

    def __str__(self):
        return f"Customer Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\n{self.shopping_cart}"


# example date
customer = Customer("Michael Daniel", "123 Main St", "michael@example.com")
customer.shopping_cart.shopping_cart()  # generate dummy shopping chart by method

# print customer
print(customer)
