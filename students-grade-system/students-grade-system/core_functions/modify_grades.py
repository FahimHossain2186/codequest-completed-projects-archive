from utility.database_print import database_print
from ui.enter import enter


def modify_grades(students):                                    #Option 4

    student_id = input("Enter studentID: ").strip()


    if student_id in students:

        student_info = students[student_id]

        while True:
            try:
                quiz_no = int(input("Please enter quiz number to modify: ").strip()) - 1
            except ValueError:
                print("Error: Quiz number must be an integer. Please try again.")
                continue
            if 0 <= quiz_no < len(student_info["grades"]):
                break

            print(f"Error: Please enter a number in between 1 and {len(student_info['grades'])}")

        while True:
            try:
                changed_grade = float(input(f"Please enter new quiz {quiz_no+1} grade: "))
            except ValueError:
                print("Error: Enter a valid grade. It must be a number")
                continue

            if 0 <= changed_grade <= 100:
                break

            print("Error: Grade must be between 0 and 100.")

        print("Before grade modification: ", end = "")
        database_print(student_id, student_info, "test")

        student_info["grades"][quiz_no] = f"{changed_grade:.1f}"
        print("After grade modification:  ", end = "")
        database_print(student_id, student_info, "test")

    else:
        print("Error: Invalid student ID")

    enter()