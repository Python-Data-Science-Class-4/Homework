class Product():
    def __init__(self, product_id='',product_name='', product_purchase_price=999, product_sale_price=777):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
        self.remarks=self.set_remarks()

    def set_remarks(self):
        if self.product_purchase_price-self.product_sale_price>0:
            return 'Profit'
        else:
            return 'Loss'
    
    def show(self):
        print(f'''
Product ID      : {self.product_id}
Product Name    : {self.product_name}
Purchase Price  : {self.product_purchase_price}
Sale Price      : {self.product_sale_price}
Remarks         : {self.remarks}''')

        
product1=Product('22Swhite42','fridge', 650, 620 )
product2=Product('22Sblack42','fridge', 875, 899 )

product1.show()
product2.show()


