from connection import Connection

class Product:
    def __init__(self):
       self.conn=Connection()
       self.cur=self.conn.getCursor()

    def create(self,name,price,category):
        query="insert into products(name,price,category) values(%s,%s,%s)"
        val=(name,price,category)
        self.cur.execute(query,val) # use execute for single record
        self.conn.getDb().commit()

    def view(self):
        query="select * from products"
        self.cur.execute(query)
        result=self.conn.getCursor().fetchall()
