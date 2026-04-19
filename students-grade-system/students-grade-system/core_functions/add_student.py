from exceptions.student_id_error import StudentIDError
from utility.test_count import test_count
from ui.enter import enter

def add_student(students):                                      #Option 6

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students.keys():
            raise StudentIDError

        else:
            student_name = input("Enter Student Name: ").strip()
            student_grades = []
            for i in range(test_count(students)):

                while True:
                    try:
                        grade = float(input(f"Enter grade for test#{i+1}: "))
                    except ValueError:
                        print("Enter a valid grade")
                        continue

                    if 0 <= grade <= 100:
                        break

                    print("Error: Grade must be between 0 and 100. Please try again.")

                student_grades.append(f"{grade:.1f}")

            students[student_id] = {"name": student_name, "grades": student_grades}

    except StudentIDError:
        print("Student ID already exists")

    enter()

