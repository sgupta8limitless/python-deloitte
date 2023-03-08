class Basic:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def printBasicDetails(self):
        print(self.__name,self.__age)

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
        