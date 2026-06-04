from add_student import add_student
from display_student import display_student
from search_student import search_student
from update_student import update_student
from delete_student import delete_student

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")