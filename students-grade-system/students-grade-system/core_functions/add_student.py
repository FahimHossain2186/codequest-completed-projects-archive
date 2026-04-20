from exceptions.student_id_error import StudentIDError
from utility.test_count import test_count
from ui.enter import enter

"""
The function prompts the user to enter a student ID and checks if the ID already exists in the system. If it does, it raises a StudentIDError. 
If the ID is unique, it prompts the user to enter the student's name and grades for each test and adds the new student information to the students dictionary.
"""

def add_student(students):                                                                  # Option 6

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students.keys():
            raise StudentIDError

        else:
            student_name = input("Enter Student Name: ").strip()
            student_grades = []
            for i in range(test_count(students)):

                while True:                                                                 # Input validation for grade
                    try:
                        grade = float(input(f"Enter grade for test#{i+1}: "))

                    except ValueError:
                        print("Enter a valid grade")
                        continue

                    if 0 <= grade <= 100:
                        break

                    print("Error: Grade must be between 0 and 100. Please try again.")

                student_grades.append(f"{grade:.1f}")                                       # Appending new student data to the dictionary

            students[student_id] = {"name": student_name, "grades": student_grades}

    except StudentIDError:
        print("Student ID already exists")

    enter()

