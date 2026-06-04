students=[]

while True:

    print("\n----------Student Management----------")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Update Student")
    print("6. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:

        student_id=int(input("enter student id:"))
        student_name=input("enter student name:")
        student_age=int(input("enter student age:"))
        student_bod=input("enter student brith of date:")


        student={
            "id":student_id,
            "name":student_name,
            "age":student_age,
            "bod":student_bod
        }

        students.append(student)
        print("Successfully added student")

    elif choice==2:

        print("\n----------Student List----------")

        for student in students:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Bod: {student['bod']}")
            print("-"*20)

    elif choice==3:

        search_id=int(input("enter student id:"))
        found= False

        for student in students:
            if student["id"]==search_id:
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Bod: {student['bod']}")

                found=True
                break
        if not found:
            print("Student not found")

    elif choice==4:
        delet_id=int(input("enter student id:"))
        found= False

        for studnet in students:
            if student["id"]==delet_id:
                students.remove(student)
                print("Successfully removed student")

                found=True
                brake
        if not found:
            print("Student not found")

    elif choice==5:
        update_id=int(input("enter student id:"))
        found=False

        for student in students:
            if student["id"]==update_id:
                student["name"]=input("enter student name:")
                student["age"]=int(input("enter student age:"))
                student["bod"]=input("enter student bod:")
                found=True
                break
        if not found:
            print("Student not found")

    elif choice==6:
        print("Thank You!")
        break

    else:
        print("Please enter a valid choice")