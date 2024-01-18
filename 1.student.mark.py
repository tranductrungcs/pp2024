def inputstu():
    n = int(input("Number student"))
    studentlist = []
    for i in range(n): 
        print(f"Student {i+1}")
        studentname = input("Name:")
        studentdob = input("DOB:")
        studentid = input("ID")
        studeninfor = {
            "Name": studentname,
            "DOB": studentdob,
            "ID": studentid,
            "Course": {}
        }
        studentlist.append(studeninfor)
    return studentlist
studentlist = inputstu()
def inputClass():
    n = int(input("Number class:"))
    classlist = []
    for i in range(n):
        print(f"Class {i+1}:")
        classname = input("Name:")
        classcode = input("Code:")
        classinfo = {
            "Name": classname,
            "Code": classcode,
        }
        classlist.append(classinfo)
    return classlist
classlist = inputClass()
def inputCourse(studentlist,classlist):
    for i, studentinfor in enumerate( studentlist):
        print(f"({i+1}) Mark - {studentinfor['Name']}:")
        for j, classinfo in enumerate(classlist):
            score = float(input(f"Mark {classinfo['Name']}:"))
            studentinfor['Course'][classinfo['Code']] = score
inputCourse(studentlist, classlist)
def printstudents(studentlist):
    print("List Student:")
    for i, studentinfor in enumerate(studentlist):
        print(f"({i+1})")
        print(f"NAME: { studentinfor['Name']}")
        print(f"DOB: {studentinfor['DOB']}")
        print(f"ID: {studentinfor['ID']}")
def printclasses(classlist):
    print("List class:")
    for i, classinfor in enumerate(classlist):
        print(f"({i+1})")
        print(f"NAME: {classinfor['Name']}")
        print(f"CODE: {classinfor['Code']}")
def Coursemark(studentlist, classlist):
    print("List mark :")
    for studentinfor in studentlist:
        print(f"Student: {studentinfor['Name']}-{studentinfor['DOB']}-{studentinfor['ID']}")
        for classinfor in classlist:
            classcode = classinfor['Code']
        else:
            classcode in studentinfor['Course']
            score = studentinfor['Course'][classcode]
            print(f"{classcode}: {score}")
while True:
    print("1 List studnet")
    print("2 List classe")
    print("3 Course mark")
    print("4 All")
    choice = input("choise")
    if choice == "1":
        printstudents(studentlist)
    elif choice == "2":
        printclasses(classlist)
    elif choice == "3":
        Coursemark(studentlist,classlist)
    elif choice == "4":
        printstudents(studentlist)
        printclasses(classlist)
        Coursemark(studentlist,classlist)
    else:
        print("Error")
