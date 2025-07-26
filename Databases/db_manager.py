import sqlite3
 
class DBManager:
    def __init__(self, db_name='student_mgmt.db'):
        self.db_name = db_name
        self.conn = None
 
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()
 
    def create_tables(self):
        cursor = self.conn.cursor()
 
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        ''')
 
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
        ''')
 
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
        ''')
 
        self.conn.commit()
 
    def get_connection(self):
        return self.conn
 
    def close(self):
        if self.conn:
            self.conn.close()