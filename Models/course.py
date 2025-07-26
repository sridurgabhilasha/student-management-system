class Course:
    def __init__(self, name, description, course_id=None):
        self.id = course_id
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"[Course] ID:{self.id}, Name: {self.name}, Description: {self.description}"
