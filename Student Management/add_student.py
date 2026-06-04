def add_student():
    import sqlite3

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    student_age = int(input("Enter Student Age: "))
    student_bod = input("Enter Student Birth Date: ")

    cursor.execute(
        """
        INSERT INTO students(id, name, age, bod)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, student_name, student_age, student_bod)
    )

    conn.commit()

    print("Student Added Successfully")

    conn.close()