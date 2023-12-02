# WEEK-5 OOP

## Question - 1
Create the class Society with following information:

Methods:
• An _init_ method to assign initial values of society_name, house_no_of_mem, flat, income
• input_data() To read information from members
• allocate_flat() To allocate flat according to income using the below table.
• show data() to display the details of the entire class.

• > =25000                A Type
• > =20000 and <25000     B Type
• >=15000 and <20000      C Type
• <15000                  D Type

## Question - 2
Define a class named "ItemInfo' with the following description:

item_code (Item Code), item (item name), price (Price of each item), qty (quantity in stock), 
discount (Discount percentage on the item), net_price (Price after discount)

Methods:
- A member method calculate_discount() to calculate discount as per the following rules:
• If qty <= 10 -> discount is 0
• If qty (11 to 20 inclusive) -> discount is 15
• If qty >= 20 -> discount is 20 
- A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and
discount to null 
- A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function
calculate_discount() to calculate the discount and net_price(price * qty - discount).
• A function show_all() or similar name to allow user to view the content of all the data members.

## Question - 3
Define a class named Product with the following specifications:

Data members:
• product_id - A string to store product.
• product_name - A string to store the name of the product.
• product_purchase_price - A decimal to store the cost price of the product.
• product_sale_price - A decimal to store Sale Price 
• Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
• Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

Methods:
• A constructor to intialize all the data members with valid default values.
• A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets
Remarks as mentioned below :
Margin         Remarks
< 0 (negative)   Loss
> 0 (positive)   Profit
• A method set_details() to accept values for product_id, product_name, product_purchase_price,
product_sale_price and invokes SetRemarks() method.
• A method get_details() that displays all the data members.

## Question - 4

Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

Class Items: Method:_init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

calculate_discount:
• total_price = price * qty
• discount -> 25% if total_price >= 4000
• discount -> 15% if total price >= 2000
• discount -> 10% if total price < 2000
• price_to_be_paid = total price - discount

shopping_cart:
Let user add items in the shopping basket. Be creative with the items, set their prices as well.

__str__():
• Print items added and total price nicely. 

Class Customer: Methods: __init__(), get_cust_info() this is optional, str()

Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in
__init__() and pass customer information as arguments while creating a customer object.

__str__(): Print customer information and price nicely. Find a way to link two classes. 
For example, instances of both classes may have a customer number. With a get method, 
get the customer number and pass it to the item object as an argument to set customer 
number attribute. So Customer class instance holds the customer info, Items class holds the
shopped item's info for the same customer ID number such as price, quantity or so. 

In the end, print both info (customer info and shopped items info) using their respective str format in a nice
way.

Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id: 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300,
price_tobe_paid: 1700]

Crate a few customers and print their information (Personal and shopping info).

## Question - 5 (Optional)

Could be a long term project as you may have time.
Create a simple game like TicTacToe or similar (Black Jack, paper-scissor-rock etc.)
Using OOP methodology
![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/f72b1724-3391-4682-81ba-f6abc5b46b67)
![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/e7fe133e-0e05-4f28-a43c-574f68a00cdc)
![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/2a1dc503-dc72-416c-b8dc-de60e86631e0)
![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/114c227a-5cca-496c-92ce-4714c04eb4fa)
![image](https://github.com/Python-Data-Science-Class-4/Homework/assets/78040636/4dcd0f9b-4178-4e51-9025-2bea111e98e6)




