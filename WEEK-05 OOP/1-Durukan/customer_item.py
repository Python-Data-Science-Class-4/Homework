class Customer():
    customer_data = dict()
    def __init__(self, customer_name="", customer_id=0):
        self.customer_name = input('Please enter the customer name: ')
        self.customer_id = len(self.customer_data) + 1
        self.customer_data[self.customer_id] = str(self.customer_id) + self.customer_name 
        print(self.customer_data)
        
    def __str__(self):
        return f'''
Customer Name: {self.customer_name}
Customer Id: {self.customer_id}
'''

class Items(Customer):
    def __init__(self, customer_name="", customer_id=0, card=[], total_price=0, discount=0):
        self.card = card
        self.total_price = total_price
        self.discount = discount
        super().__init__(customer_name, customer_id)
        self.shopping_card()
    
    def __str__(self):
        return f'''
Customer Name: {self.customer_name}
Customer Id: {self.customer_id}
Card: {self.card}
Total Price: {self.total_price}
Discount: {self.discount}
Payed Amount: {self.price_tobe_paid}
'''

    def shopping_menu(self):
        selection = input('''
1 -> Add Item
2 -> Display card
                
''')
        

    


    def calculate_discount(self):
        if self.total_price < 2000:
            self.discount = 10
        elif 2000 <= self.total_price < 4000:
            self.discount = 15
        else:
            self.discount = 25 
        
        self.price_tobe_paid = self.total_price*((100-self.discount)/100)

    def shopping_card(self):
        while True:
            choice = input('Do you want to add new item to the cart? Yes(y) / No(n): ')
            if choice == "y":
                item_name = input('Please enter the item name you buy: ')
                item_qty = int(input('Please enter the amount of this item:  '))
                item_price = float(input('Please enter the price of each: '))
                self.card.append([item_name, item_price, item_qty])
                print(self.card)
                self.get_total_amount(item_qty, item_price)
            elif choice == "n":
                self.calculate_discount()
                self.customer_data[self.customer_id] = self.__str__()
                print(self.__str__())
                break
            else:
                print('Invalid choice')        


    def get_total_amount(self, item_qty, item_price):
        self.total_price += item_qty*item_price



def shopping_algorithm():
    print("Welcome to the shopping center :) ")
    while True:
        selection = input('''
Please make a selection:
    1 -> Create Account
    2 -> Start shopping
    q -> Quit
Selection: ''')
        if selection == "1":
            user = Customer()
            # print(user)

        elif selection == "2":
            shop = Items()

shopping_algorithm()

''' Kod harika,ellerinize saglik. Bir oneri;
**price_tobe_paid değişkenini __init__ metodunda tanımlamak ve ardından calculate_discount fonksiyonunda güncellemek daha uygun olabilir.'''

    


