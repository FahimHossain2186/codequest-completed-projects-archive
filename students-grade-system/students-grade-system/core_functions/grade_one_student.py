from ui.enter import enter
from utility.database_print import database_print
from ui.header import header

def grade_one_student(students):                                #Option 2

    student_id = input("Enter studentID: ").strip()

    if student_id in students:
        header(students, "test")
        student_info = students[student_id]
        print()
        database_print(student_id, student_info, "test")

    else:
        print("Error: Invalid student ID")

    enter()