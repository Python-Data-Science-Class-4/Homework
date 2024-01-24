class Society():
    #Created a class as known "society", we need to take from some informations about the members.
    #firstly created normally init method, and assigned initial values 
    def __init__(self,society_name="",house_no_of_mem="",flat="",income=0) :
        self.society_name=society_name 
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
        
        self.input_data() 
        self.allocate_flat()
    
    def input_data(self):
        #inputs form members
        self.society_name = str(input("Society Name:"))
        self.house_no_of_mem= str(input("No:"))
        self.income=int(input("Income:"))
        
    def allocate_flat(self): # It assigns to which type it is based on the conditions
        if self.income >= 2500 :
            self.flat= "A Type" 
        elif 2000 <= self.income < 2500 :
            self.flat= "B type"
        elif 1500 <= self.income < 2000:
            self.flat= " C type" 
        else:
            self.flat="D type"
            
    def show_data(self):
        #it shows the data from member
        return ("Society Name: {}\nHouse no of member:{}\nIncome:{}\nFlat Type:{}\n".format(self.society_name,self.house_no_of_mem,self.income,self.flat))

person1= Society() # created a object for example

print(person1.show_data())

''' Kod gayet basarili tebrik ederim. Sadece bir kac onerim olabilir.
**__init__ fonksiyonunda zaten değerleri aldığınız için input_data fonksiyonu aslinda cpk da gerekli değil. 
 __init__ içinde doğrudan değer ataması yapabilirsiniz. 
 soyle ki;
 person1 = Society(
    society_name=input("Society Name: "),
    num_of_members=int(input("Number of Members: ")),
    income=int(input("Income: "))
)
input_data fonksiyonunu kaldirip sonucu bu sekilde yapabilirsiniz.

** show data fonksiyonundaki ciktiyi soyle daha duzenli sekilde yazabilirsiniz.
return f"Society Name: {self.society_name}\nNumber of Members: {self.num_of_members}\nIncome: {self.income}\nFlat Type: {self.flat_type}\n"
'''

