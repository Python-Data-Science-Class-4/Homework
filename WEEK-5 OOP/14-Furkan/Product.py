class Product:
    def __init__(self, product_id='', product_name='', 
                 product_purchase_price=0.0, product_sale_price=0.0):
        self.id = product_id
        self.name = product_name
        self.purchase = product_purchase_price
        self.sale = product_sale_price
        self.calculate_margin()
        self.set_remarks()

    def calculate_margin(self):
        self.margin = round(self.sale - self.purchase)

    def set_remarks(self):
        if self.margin > 0:
            self.remarks = "Profit"
        elif self.margin < 0:
            self.remarks = "Loss"
        else:
            self.remarks = "Neither profit nor loss"

# Example usage:
product1 = Product(product_id="BJK", product_name="T-shirt", 
                   product_purchase_price=60.0, product_sale_price=94.9)
Example = (f'''           
           Product ID:         {product1.id} 
           Product name:       {product1.name} 
           Purchase price:     {product1.purchase} Euro
           Sale price:         {product1.sale} Euro
           Amount of margin:   {product1.margin} Euro
           Remarks:            {product1.remarks}''')
print (Example)

''' Kod gayet guzel tebrik ederim.'''
