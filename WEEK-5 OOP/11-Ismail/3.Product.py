class Product():
    #firstly created normally init method, and assigned initial values.
    def __init__(self,product_id="",product_name="",product_sale_price=0,product_purchase_price=0):
        self.product_id = input("Product Id:")
        self.product_name = input("Product Name:")
        self.product_sale_price = int(input("Product Sale Price :"))
        self.product_purchase_price = int(input("Product Purchase Price :"))
        #Created "input" every single info to take information of product from the user.
        
        self.remarks=self.set_remarks
        
    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price > 0: 
        #It will print  "Profit" ; if the sale price of product is bigger than purchase price of product.
            return 'Profit'
        elif self.product_sale_price - self.product_purchase_price < 0:
            return 'Loss'
        else:
            return 'None'
        
    def show_dat(self):
        return("Product ID :{}\nProduct Name : {}\nProduct Sale Price :{}\nProduct Purchase Price: {}\nRemarks : {}".format(self.product_id,self.product_name,self.product_sale_price,self.product_purchase_price,self.remarks()))      
        

product121=Product()
print(product121.show_dat())