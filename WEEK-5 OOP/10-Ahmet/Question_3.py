class Product():
    def __init__(self, product_id, product_name, product_purchase_price, product_sale_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.remarks = self.set_remarks()

    def set_remarks(self):
        if (self.product_purchase_price) - (self.product_sale_price) > 0:
            return "Profit"
        else:
            return "Loss"
    
    def show(self):
        print(f"Product ID: {self.product_id}\nroduct Name: {self.product_name}\nPurchase Price: {self.product_purchase_price} Euro\nSale Price: {self.product_sale_price} Euro\nRemarks: {self.remarks}")

        
product1 = Product('22Flat-S13','Monitor', 210, 224 )

product1.show()