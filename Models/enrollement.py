class Enrollement:
    def __init__(self, student_id, course_id, enrollement_id):
        self.id = enrollement_id
        self.student_id = student_id
        self.course_id = course_id
    
    def __str__(self):
        return f"[Enrollement] ID: {self.id}, Student ID: {self.student_id}, Course ID: {self.course_id}"
    