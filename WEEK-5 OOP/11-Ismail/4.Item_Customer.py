import random
import string 

class Customer():
    customer_info = {}

    def __init__(self, customer_name="", customer_surname="", customer_id="" ):
        self.customer_name = input("Name: ")
        self.customer_surname = input("Surname: ")
        self.operation_code = self.operation_code_creator()
        self.customer_id = self.customer_id_creator()
        self.customer_info[self.customer_id] = (self.customer_name, self.customer_surname)
        

    def customer_id_creator(self): 
        '''This function is creating an ID with first two letters of user's name and surname '''
        name_id = self.customer_name[:2].upper()
        surname_id = self.customer_surname[:2].upper()
        created_id = name_id + "---" + surname_id + "---"
        print (created_id)
        return  created_id
    
    def operation_code_creator(self):
        '''This function is creating an uniqe code for every operation'''
        operation_code=""
        letters=string.ascii_uppercase
        numbers = string.digits
        created_code= letters +numbers
        for _ in range(11):
            digit = random.choice(created_code)
            operation_code += digit
        return operation_code
    
class Items(Customer):
    def __init__(self):
        self.total_price = 0
        self.discount = 0
        self.product_cards = []
        super().__init__()
        self.shopping_card()

    def shopping_card(self):
        '''This function takes some informations from the users about the products'''
        while True:
            product_name = input("Product Name: ")
            product_qty = int(input("Product Quantity: "))
            product_price = float(input("Product Price: "))
            self.product_cards.append([product_name, product_qty, product_price])

            add_more = input("Add more items? (Y/N): ")
            if add_more.upper() != 'Y':
                break

        self.calculate_discount()

    def calculate_discount(self):
        '''This function calculates a discount depending on how much total price is'''
        for item in self.product_cards:
            self.total_price += item[1] * item[2]

        if self.total_price < 2000:
            self.discount = 10
        elif self.total_price < 4000:
            self.discount = 15
        else:
            self.discount = 25 

        self.price_to_be_paid = self.total_price * ((100 - self.discount) / 100)

    def __str__(self):
        '''This function shows that the information from users, in addition it shows discount and prices'''
        for item in self.product_cards:
            items=""
            product_name = item[0]
            quantity = item[1]
            price = item[2]
            item_str = f"Name: {product_name} - Quantity: {quantity}, Price: {price}"
            items += item_str
        return f'''
Customer Name: {self.customer_name}
Customer Surname: {self.customer_surname}
Customer ID: {self.customer_id}

Shopping Card:
Operation Code: {self.operation_code}
{items}

Total Price: {self.total_price}
Discount: {self.discount}%
Price to be Paid: {self.price_to_be_paid}
'''

customer1= Items()
print(customer1)
