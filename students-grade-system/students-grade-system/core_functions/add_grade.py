from ui.enter import enter
from utility.test_count import test_count

'''
This function adds a new grade for all students in the system.
The function collects the grades for each student.
If the input is valid, it adds the grade to the student's list of grades. Finally, it calls the enter function to pause the program and wait for the user to press Enter before returning to the main menu.
'''

def add_grade(students):                                                                            # Option 5

    if not students:                                                                                # If there are no students, it prints a message and returns.
        print("No students in the system.")
        enter()
        return

    test_number = test_count(students)
    print(f"Please enter test grades for Test#{test_number+1}\n")
                                                                                
    # It initializes an empty temporary dictionary to store the new collected grades for each student. 
    # The keys of this dictionary will be the student IDs, and the values will be the corresponding grades for the new test.

    '''
    The style we used for collected dictionary is:

        collected = {
            "student_id1": "85.0",
            "student_id2": "90.0"
        }
    '''

    collected = {}  

    #for student_id, _ in students.items(): 
    # _ represents the student information, which is not used in this function.

    for student_id in students.keys():

        while True:
            try:
                grade = float(input(f"Please enter grade for student : {student_id}\n").strip())

                if not (0 <= grade <= 100):                                                         # It validates that the input is a numeric value between 0 and 100.
                    print("Error: Grade must be between 0 and 100. Please try again.")
                    continue

            except ValueError:
                print("Error: Please enter a numeric grade.")
                continue

            collected[student_id] = f"{grade:.1f}"
            break

    # Appending the collected values to dictionary
    for student_id, grade_str in collected.items():
        while len(students[student_id]["grades"]) < test_number:
            students[student_id]["grades"].append(" ")
        students[student_id]["grades"].append(grade_str)

    enter()