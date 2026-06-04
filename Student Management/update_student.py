def update_student():
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

        new_name = input("Enter New Name: ")
        new_age = int(input("Enter New Age: "))
        new_bod = input("Enter New Birth Date: ")

        cursor.execute(
            """
            UPDATE students
            SET name = ?, age = ?, bod = ?
            WHERE id = ?
            """,
            (new_name, new_age, new_bod, student_id)
        )

        conn.commit()

        print("Student Updated Successfully")

    else:
        print("Student Not Found")

    conn.close()