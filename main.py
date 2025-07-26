from Databases.db_manager import DBManager
from Services.student_service import StudentService
from Services.course_service import CourseService
from Services.enrollement_service import EnrollmentService
from Models.student import Student
from Models.course import Course
# from Models.enrollement import Enrollement

def print_menu():
    print("\n========= Student Management System =========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Course")
    print("6. View All Courses")
    print("7. Update Course")
    print("8. Delete Course")
    print("9. Enroll Student in Course")
    print("10. View Students in a Course")
    print("11. View Courses of a Student")
    print("12. Unenroll Student from Course")
    print("0. Exit")

def main():
    db = DBManager()
    db.connect()

    student_service = StudentService(db.get_connection())
    course_service = CourseService(db.get_connection())
    enrollment_service = EnrollmentService(db.get_connection())

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == '1':
                name = input("Student Name: ")
                age = int(input("Age: "))
                email = input("Email: ")
                student = Student(name, age, email)
                student_service.add_student(student)
                print("✅ Student added.")

            elif choice == '2':
                students = student_service.get_all_students()
                if students:
                    for s in students:
                        print(s)
                else:
                    print("No students found.")

            elif choice == '3':
                sid = int(input("Enter Student ID to update: "))
                student = student_service.get_student(sid)
                if student:
                    student.name = input(f"New Name [{student.name}]: ") or student.name
                    student.age = int(input(f"New Age [{student.age}]: ") or student.age)
                    student.email = input(f"New Email [{student.email}]: ") or student.email
                    student_service.update_student(student)
                    print("✅ Student updated.")
                else:
                    print("❌ Student not found.")

            elif choice == '4':
                sid = int(input("Enter Student ID to delete: "))
                student_service.delete_student(sid)
                print("✅ Student deleted.")

            elif choice == '5':
                name = input("Course Name: ")
                desc = input("Course Description: ")
                course = Course(name, desc)
                course_service.add_course(course)
                print("✅ Course added.")

            elif choice == '6':
                courses = course_service.get_all_courses()
                if courses:
                    for c in courses:
                        print(c)
                else:
                    print("No courses found.")

            elif choice == '7':
                cid = int(input("Enter Course ID to update: "))
                course = course_service.get_course(cid)
                if course:
                    course.name = input(f"New Name [{course.name}]: ") or course.name
                    course.description = input(f"New Desc [{course.description}]: ") or course.description
                    course_service.update_course(course)
                    print("✅ Course updated.")
                else:
                    print("❌ Course not found.")

            elif choice == '8':
                cid = int(input("Enter Course ID to delete: "))
                course_service.delete_course(cid)
                print("✅ Course deleted.")

            elif choice == '9':
                sid = int(input("Student ID: "))
                cid = int(input("Course ID: "))
                enrollment_service.enroll_student(sid, cid)
                print("✅ Enrollment successful.")

            elif choice == '10':
                cid = int(input("Course ID: "))
                students = enrollment_service.get_students_by_course(cid)
                if students:
                    for s in students:
                        print(f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Email: {s[3]}")
                else:
                    print("No students enrolled in this course.")

            elif choice == '11':
                sid = int(input("Student ID: "))
                courses = enrollment_service.get_courses_by_student(sid)
                if courses:
                    for c in courses:
                        print(f"ID: {c[0]}, Name: {c[1]}, Description: {c[2]}")
                else:
                    print("This student is not enrolled in any courses.")

            elif choice == '12':
                sid = int(input("Student ID: "))
                cid = int(input("Course ID: "))
                enrollment_service.unenroll_student(sid, cid)
                print("✅ Student unenrolled from course.")

            elif choice == '0':
                print("Exiting... Goodbye!")
                db.close()
                break

            else:
                print("❌ Invalid option. Try again.")

        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()