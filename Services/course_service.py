from Models.course import Course

class CourseService:
    def __init__(self, db_conn):
        self.conn = db_conn

    def add_course(self, course: Course):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO courses (name, description) VALUES (?, ?)",
            (course.name, course.description)
        )
        self.conn.commit()
        course.id = cursor.lastrowid
        return course

    def get_course(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        if row:
            return Course(row[1], row[2], course_id=row[0])
        return None

    def get_all_courses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        return [Course(row[1], row[2], course_id=row[0]) for row in rows]

    def update_course(self, course: Course):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE courses SET name = ?, description = ? WHERE id = ?",
            (course.name, course.description, course.id)
        )
        self.conn.commit()

    def delete_course(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        self.conn.commit()