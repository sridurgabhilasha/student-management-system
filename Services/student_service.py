from Models.student import Student

class StudentService:
    def __init__(self, db_conn):
        self.conn = db_conn

    def add_student(self, student: Student):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
            (student.name, student.age, student.email)
        )
        self.conn.commit()
        student.id = cursor.lastrowid
        return student

    def get_student(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()
        if row:
            return Student(row[1], row[2], row[3], student_id=row[0])
        return None

    def get_all_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [Student(row[1], row[2], row[3], student_id=row[0]) for row in rows]

    def update_student(self, student: Student):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?",
            (student.name, student.age, student.email, student.id)
        )
        self.conn.commit()

    def delete_student(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
