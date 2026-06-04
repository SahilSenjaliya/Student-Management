from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Management API"}

@app.get("/students")
def get_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    bod: str


@app.post("/students")
def add_student(student: Student):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students(id,name,age,bod) VALUES(?,?,?,?)",
            (student.id, student.name, student.age, student.bod)
        )

        conn.commit()

        return {"message": "Student Added Successfully"}

    except sqlite3.IntegrityError:
        return {"error": "Student ID already exists"}

    finally:
        conn.close()

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    existing_student = cursor.fetchone()

    if not existing_student:
        conn.close()
        return {"error": "Student Not Found"}

    cursor.execute(
        """
        UPDATE students
        SET name=?, age=?, bod=?
        WHERE id=?
        """,
        (student.name, student.age, student.bod, student_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Student Updated Successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        conn.close()
        return {"error": "Student Not Found"}

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Student Deleted Successfully"}