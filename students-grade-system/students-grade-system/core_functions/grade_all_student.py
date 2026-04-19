from ui.enter import enter
from utility.database_print import database_print
from ui.header import header

def grade_all_student(students):                                #Option 1

    if not students:                            # students == ""
        print("No dataset for Students")
        return

    header(students, "test")
    print("\n")

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "test")

    enter()