def delete_student():
    import sqlite3

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to delete: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        conn.commit()

        print("Student Deleted Successfully")

    else:
        print("Student Not Found")

    conn.close()