def search_student():
    import sqlite3

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Bod: {student[3]}")
    else:
        print("Student Not Found")

    conn.close()