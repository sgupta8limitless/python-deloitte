from basic import Basic

class Student(Basic):

    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.__course=course
        

    def printDetails(self):
      self.printBasicDetails()
      print(self.__course)

    




    







