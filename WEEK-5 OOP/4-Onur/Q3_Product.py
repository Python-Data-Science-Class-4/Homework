"![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/2a1dc503-dc72-416c-b8dc-de60e86631e0)"

class Product:
    def __init__(self,product_name ="New_Product",purchase_price = 100, sale_price = 120) :
        self.product_id = Product.next()
        self.product_name = product_name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.margin = self.sale_price - self.purchase_price
        self.remarks = self.__set_remarks()


    #we need to create a variable to store the order of the product id
    next_id = 1

    # by calling this method, we set new product_id for each product created.
    @classmethod
    def next():
        next += 1
        return next-1

    def __set_remarks(self):
        if self.sale_price - self.purchase_price >= 0:
            return "Profit"
        else:
            return "Loss"
