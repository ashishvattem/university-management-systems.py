class Person:
    def __init__(self,roll,name,mobile):
        self.roll = roll
        self.name = name
        self.mobile = mobile
class Student(Person):
    def __init__(self,roll,name,mobile,branch):
        self.branch = branch
        super.__init__(roll,name,mobile)
class Teacher(Person):
    def __init__(self,roll,name,mobile,subject):
        self.subject = subject
        super.__init__(roll,name,mobile)
class College(Person):
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
colleges = []
while True:
    print("Choose your option: ")
    print("1. Create college: ")
    print("2. Add student: ")
    print("3. Add Teacher: ")
    print("4. Display students details")
    print("5. Display Teachers details")
    print("6. Exit")
    if x == 1:
        cname = input("Enter the college  Name: ")
        n = True
        for i in colleges:
            if i.name == cname:
                n = False
                break
        if n == False:
            print()
            print("College name already Exists !")
            print()
        else:
            college = College(cname)
            colleges.append(college)
            print()
            print("College Created Successfully ")
            print()
    elif x == 2:
        cname = input("Enter College name: ")
        n = True
        obj = None
        for i in colleges:
            if i.name == cname:
                n = False
                obj = i
                break
        if n == True:
            print()
            print(f"College with name {cname} does not Exist !")
            print()
        else:
            roll = input("Enter Student Roll Number: ")
            name = input("Enter Student name : ")
            mobile = input("Enter Student Mobile number: ")
            branch = input("Enter Student Branch : ")
            s = Student(roll,name,mobile,branch)
            obj.add_student(s)
            print()
            print("Student Data Stored Sucessfully")
            print()
     elif x == 3:
        cname = input("Enter College name: ")
        n = True
        obj = None
        for i in colleges:
            if i.name == cname:
                n = False
                obj = i
                break
        if n == True:
            print()
            print(f"College with name {cname} does not Exist !")
            print()
        else:
            roll = input("Enter Teacher Roll Number: ")
            name = input("Enter Teacher name : ")
            mobile = input("Enter Teacher Mobile number: ")
            subject = input("Enter Teacher Subject : ")
            s = Teacher(roll,name,mobile,subject)
            obj.add_teacher(s)
            print()
            print("Teacher Data Stored Sucessfully")
            print()
     elif x == 4:
        cname = input("Enter College name: ")
        n = True
        obj = None
        for i in colleges:
            if i.name == cname:
                n = False
                obj = i
                break
        if n == True:
            print()
            print(f"College with name {cname} does not Exist !")
            print()
        else:
            print(f"Student details if {cname} are: ")
            print()
            for k in obj.students:
                print(f"Roll: {k.roll}")
                print(f"Name: {k.name}")
                print(f"Mobile: {k.mobile}")
                print(f"Branch: {k.branch}")
                print()
     elif x == 5:
        cname = input("Enter College name: ")
        n = True
        obj = None
        for i in colleges:
            if i.name == cname:
                n = False
                obj = i
                break
        if n == True:
            print()
            print(f"College with name {cname} does not Exist !")
            print()
        else:
            print(f"Teachers details if {cname} are: ")
            print()
            for k in obj.teachers:
                print(f"Roll: {k.roll}")
                print(f"Name: {k.name}")
                print(f"Mobile: {k.mobile}")
                print(f"Subject: {k.subject}")
                print()
    elif x == 6:
        break
    else:
        print("Choose the Correct Option !")
