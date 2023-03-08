import mysql.connector

# create a connection 
db=mysql.connector.connect(host="localhost",port="3307",user="root",password="thorabh8",database="inventory")

# create a cursor 
cursor=db.cursor()

# this is fetch all records 

# query="select * from products"
# cursor.execute(query)

# result=cursor.fetchall()

# for row in result:
#     print(row)

# fethcing based on filters 

# id=int(input("Enter Id "))
# query="select * from products where id=%s"
# val=[id]

# cursor.execute(query,val)

# result=cursor.fetchone()

# print(result)

# insert record 

# query="insert into products(name,price,category) values(%s,%s,%s)"
# val=[
#     ('Product 5',3000,'Accesories'),
#     ('Product 6',3200,'Accesories'),
#     ('Product 7',3000,'Accesories')
# ]

# cursor.executemany(query,val) # use execute for single record

# db.commit()

# print(cursor.lastrowid)

# delete record 
# query="delete from products where id in (%s,%s)"
# val=[7,9]

# cursor.execute(query,val)

# db.commit()
n=1
while(n==1):
    print("Choose an option ")
    print("1. Add Product")
    print("2. View Product")
    print("3. Delete Product")
    print("4. Update Product")
    choice=int((input()))

    if(choice==1):
        name=str(input("Enter Product Name "))
        price=int(input("Enter Price "))
        category=str(input("Enter Category "))
        query="insert into products(name,price,category) values(%s,%s,%s)"
        val=(name,price,category)
        cursor.execute(query,val) # use execute for single record
        db.commit()
    elif(choice==2):
        query="select * from products"
        cursor.execute(query)
        products=cursor.fetchall()
        for product in products:
            print(product)

    n=int(input("Do you want to continue 1-yes 0-no"))









