class Product():
    def __init__(self, product_id='',product_name='', product_purchase_price=0, product_sale_price=0):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
        self.profit=self.set_remarks()

    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price > 0:
            return 'Profit'
        elif self.product_sale_price - self.product_purchase_price < 0:
            return 'Loss'
        else:
            return 'None'
    
    def show_data(self):
        print(f'''
Product ID      : {self.product_id}
Product Name    : {self.product_name}
Purchase Price  : {self.product_purchase_price}
Sale Price      : {self.product_sale_price}
Profits         : {self.profit}''')

''' Kod gayet guzel,
**show_data fonksiyonu sadece bilgi göstermek için kullanılıyorsa bu tür fonksiyonlara genellikle __str__ metodu eklemek daha uygun olabilir.
**koddan hicbir çıktı alamıyoruz herhangi bir product tanımlayabilirsiniz onu görebiliriz'''
