class Customer():
     
   
    def __init__(self, factory_name=None, factory_type=None) -> None:
        self.factory_name=factory_name
        self.factory_type=factory_type
        self.get_cust_info()

    def get_cust_info(self):
        self.factory_name=input('Please enter the factory name:')
        self.factory_type=input('Please enter the factory type (A,B,C):')

class Items(Customer):
    def __init__(self, factory_name=None, factory_type=None, product=None, qty=None, price=None):
        super().__init__(factory_name, factory_type)
        self.product=product
        self.qty=qty
        self.price=price
        self.shopping_card()
        self.discount=self.calculate_discount()
        self.price_tobe_paid=self.get_total_amount()

    def calculate_discount(self):
        discount=0
        total_price=0
        total_price=Items.sum_price*Items.sum_qty
        if total_price>=4000:
            discount=0.25
        elif total_price>=2000:
            discount=0.15
        elif total_price<2000:
            discount=0.10
        return discount

    product_list=[]
    sum_qty=0
    sum_price=0
    def shopping_card(self):
        
        while True:
            self.product=input("Please enter the product name:")
            self.qty=float(input("Please enter the product quantity:"))
            self.price=float(input("Please enter the product price:"))
            a=input("To end the cart press 'Yes'.To contunie 'No':")
            Items.product_list.append(self.product)
            Items.sum_qty+=self.qty
            Items.sum_price+=self.price
            if a.lower()=='yes':
                break
    
    def get_total_amount(self):
        price_tobe_paid=(1-self.discount)*Items.sum_price*Items.sum_qty
        return price_tobe_paid

    
    def __str__(self):
        return f'''
Factory Name            :{self.factory_name}
Factory Type            :{self.factory_type}
Product Name            :{Items.product_list} 
Total Product Quantity  :{Items.sum_qty}
Total Product Price     :{Items.sum_price}
Discount                :{self.discount}
Amount to be paid       :{self.price_tobe_paid}'''


items1=Items()
print(items1.__str__())