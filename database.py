import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_student(self, student):
        query = "INSERT INTO students (name, grade) VALUES (?, ?)"
        self.conn.execute(query, (student.name, student.grade))
        self.conn.commit()

    def view_students(self):
        cursor = self.conn.execute("SELECT * FROM students")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")

    def update_student(self, student_id, student):
        query = "UPDATE students SET name = ?, grade = ? WHERE id = ?"
        self.conn.execute(query, (student.name, student.grade, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = ?"
        self.conn.execute(query, (student_id,))
        self.conn.commit()
