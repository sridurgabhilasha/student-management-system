from Models.enrollement import Enrollement

class EnrollmentService:
    def __init__(self, db_conn):
        self.conn = db_conn

    def enroll_student(self, student_id, course_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )
        self.conn.commit()
        enrollement_id = cursor.lastrowid
        return Enrollement(student_id, course_id, enrollment_id=enrollement_id)

    def get_students_by_course(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT s.id, s.name, s.age, s.email FROM students s
        JOIN enrollments e ON s.id = e.student_id
        WHERE e.course_id = ?
        """, (course_id,))
        return cursor.fetchall()

    def get_courses_by_student(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT c.id, c.name, c.description FROM courses c
        JOIN enrollments e ON c.id = e.course_id
        WHERE e.student_id = ?
        """, (student_id,))
        return cursor.fetchall()

    def unenroll_student(self, student_id, course_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM enrollments WHERE student_id = ? AND course_id = ?
        """, (student_id, course_id))
        self.conn.commit()
