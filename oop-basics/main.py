from student import Student
from teacher import Teacher

students=[]
n=1
while(n==1):
    print("Slect a operation")
    print("1. Add Student")
    print("2. View Students")
    print("3. Sort By Age & View")
    print("4. Search By Keyword")
    choice=int(input())

    if(choice==1):
        name=str(input("Enter Student Name "))
        age=int(input("Enter Student Age "))
        course=str(input("Enter Student Course "))
        students.append(Student(name,age,course))
    elif(choice==2):
        for studentObj in students:
            studentObj.printDetails()
    elif(choice==3):
        students.sort(key=lambda s:s.getAge())
        for studentObj in students:
            studentObj.printDetails()
    elif(choice==4):
        keyword=str(input("Enter Search Term "))
        slist=[student for student in students if keyword.lower() in student.getName().lower()]
        if(len(slist)!=0):
            for studentObj in slist:
                studentObj.printDetails()
        else:
            print("No Such Student")
        # count=0
        # for student in students:
        #     if(keyword.lower() in student.getName().lower()):
        #         print(student.printDetails())
        #         count+=1
            
        # if(count==0):
        #     print("No Such Student")
    else:
        print("Invalid Option")
    n=int(input("do you want to continue 1-yes 0-no"))


