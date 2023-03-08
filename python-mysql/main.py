from product import Product

p=Product()


name=str(input("Enter Product Name "))
price=int(input("Enter Price "))
category=str(input("Enter Category "))
p.create(name,price,category)
