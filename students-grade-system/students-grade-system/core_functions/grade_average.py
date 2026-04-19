from ui.enter import enter
from utility.database_print import database_print
from ui.header import header

def grade_average(students):                                    #Option 3

    header(students, "avg")
    print()

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "avg")

    enter()