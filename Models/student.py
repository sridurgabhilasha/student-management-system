class Student:
    def __init__(self, name, age, email, student_id=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email
    
    def __str__(self):
        return f"[Student] ID:{self.id}, Name: {self.name}, Age: {self.age}, Email: {self.email}"
