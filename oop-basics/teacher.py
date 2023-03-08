from basic import Basic
class Teacher(Basic):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.__dept=dept

    def printDetails(self):
        self.printBasicDetails()
        print(self.__dept)
       