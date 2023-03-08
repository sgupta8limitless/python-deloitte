class Demo:
    def __init__(self):
       self.id=22
       self.city="Mumbai"

    def printInfo(self):
        # self.id=22
        # self.city="Mummbai"
        print(self.id,self.city)



class NewChild(Demo):

    def __init__(self):
        super().__init__()
    
    # def __init__(self):
    #     super().__init__()
    
        

    def printDetails(self):
        self.name="Vikrant"
        print(self.name)
        


nc=NewChild()
nc.printInfo()
nc.printDetails()