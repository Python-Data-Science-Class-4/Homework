class Product():
    def __init__(self, product_id="", product_name="", product_purchase_price=0, product_sale_price=0):
        self.product_id = input( "please enter the product id: ")
        self.product_name = input("please enter the product name: ")
        self.product_purchase_price = int(input("please enter purchase price of the product: "))
        self.product_sale_price = int(input("please enter sale price of the product: "))
        self.remarks = self.set_remarks()
        print(self.show_all())

    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price > 0:
            self.remarks = "Profit"
            return self.remarks
        elif self.product_sale_price - self.product_purchase_price < 0:
            self.remarks = "Loss"
            return self.remarks
        else:
            return "None"

    def show_all(self):
        print(f'''
ProductId      : {self.product_id}
ProductName    : {self.product_name}
Purchase Price : {self.product_purchase_price}
SalePrice      : {self.product_sale_price}
SetRemarks     : {self.remarks}''')


product1 = Product()

