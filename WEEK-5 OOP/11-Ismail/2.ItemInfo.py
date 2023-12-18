class ItemInfo():
    discount_type1= 0.8 
    '''created two type of discount in here. Because if we want to change for a while time, it will be easy.'''
    discount_type2=0.75
    
    def __init__(self,item_code="",item="",price=0,qty=0,discount=0,net_price=0):
        self.item_code=item_code
        self.item= item
        self.price= price
        self.qty= qty
        self.discount= discount
        self.net_price=net_price
        
        self.get_purchase()
        self.calculate_discount()
        self.show_all()
    
    def get_purchase(self):
        
        '''This function takes the info from the users''' 
        
        self.item_code = str(input("Please enter your item CODE: "))
        self.item = str(input("Please enter the item NAME: "))
        self.price = int(input('Please enter the PRICE:'))
        self.qty = int(input("Please enter the QUANTITY: "))
        
    def calculate_discount(self): 
        
        '''This function calculate the discount how much is'''
        
        if self.qty >= 20:
            self.net_price= self.price*(ItemInfo.discount_type1)
            
        elif 10 < self.qty < 20:
            self.net_price= self.price*(ItemInfo.discount_type2)
            
        else:
            self.net_price=self.price
            
    
    def show_all(self):
        '''This function provides that shows the all outputs'''
        return f"Code : {self.item_code}\nItem Name:{self.item}\nPrice:{self.price}\nQuantity:{self.qty}\nNet Price:{self.net_price}" 

    
item1=ItemInfo()

print(item1.show_all())