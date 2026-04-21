from utility.database_print import database_print
from ui.enter import enter

'''
This module allows the user to modify the grades of a specific student.
'''


def modify_grades(students):                                                                        # Option 4

    student_id = input("Enter studentID: ").strip()

    '''
        It checks if the student ID exists in the system. 
        If it does, it allows the user to modify the grades of that student. 
        If the ID doesn't exist, it raises an error message.
    '''

    if student_id in students:                                                                      # Checking if the student ID exists in the keys of the students dictionary                                                                          
        
        student_info = students[student_id]

        if not student_info["grades"]:
            print("Error: This student has no grades to modify.")
            enter()
            return

        # Input validation for quiz number
        while True:                                                     

            try:
                quiz_no = int(input("Please enter quiz number to modify: ").strip()) - 1
            
            except ValueError:
                print("Error: Quiz number must be an integer. Please try again.")
                continue
            
            if 0 <= quiz_no < len(student_info["grades"]):
                break

            print(f"Error: Please enter a number in between 1 and {len(student_info['grades'])}")


        # Input validation for grade
        while True:

            try:
                changed_grade = float(input(f"Please enter new quiz {quiz_no+1} grade: "))
            
            except ValueError:
                print("Error: Enter a valid grade. It must be a number")
                continue

            if 0 <= changed_grade <= 100:
                break

            print("Error: Grade must be between 0 and 100.")


        # It prints the student's information before and after the grade modification to show the changes made.
        
        print("Before grade modification: ", end = "")
        database_print(student_id, student_info, "test")

        student_info["grades"][quiz_no] = f"{changed_grade:.1f}"
        print("After grade modification:  ", end = "")
        database_print(student_id, student_info, "test")

    else:
        print("Error: Invalid student ID")

    enter()