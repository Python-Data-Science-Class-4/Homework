class Product:
    def __init__(self, product_id="", product_name="", product_purchase_price=0.0, product_sale_price=0.0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.margin = 0.0
        self.remarks = ""
        self.set_remarks()

    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price
        if self.margin > 0:
            self.remarks = "Profit"
        elif self.margin < 0:
            self.remarks = "Loss"
        else:
            self.remarks = "No Profit or Loss"


product1 = Product("P001", "Laptop", 800.0, 1200.0)
print("Product ID:", product1.product_id)
print("Product Name:", product1.product_name)
print("Purchase Price:", product1.product_purchase_price)
print("Sale Price:", product1.product_sale_price)
print("Margin:", product1.margin)
print("Remarks:", product1.remarks)
