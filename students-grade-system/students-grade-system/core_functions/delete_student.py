from exceptions.student_id_error import StudentIDError
from ui.enter import enter

def delete_student(students):                                   #Option 7
    try:
        student_id = input("Enter studentID: ").strip()

        if not student_id in students.keys():
            raise StudentIDError

        else:
            students.pop(student_id)

    except StudentIDError:
        print("Student ID doesn't exist")

    enter()

