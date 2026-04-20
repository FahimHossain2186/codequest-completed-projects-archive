from exceptions.student_id_error import StudentIDError
from ui.enter import enter

'''
The function prompts the user to enter a student ID and checks if the ID exists in the system. 
If it does, it removes the student from the system. If the ID doesn't exist, it raises a StudentIDError.
'''

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

