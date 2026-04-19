from ui.enter import enter
from utility.test_count import test_count

def add_grade(students):                                        #Option 5

    if not students:
        print("No students in the system.")
        enter()
        return

    test_number = test_count(students)
    print(f"Please enter test grades for Test#{test_number+1}\n")

    collected = {}

    for student_id, student_info in students.items():
        while True:
            try:
                grade = float(input(f"Please enter grade for student : {student_id}\n").strip())

                if not (0 <= grade <= 100):
                    print("Error: Grade must be between 0 and 100. Please try again.")
                    continue

            except ValueError:
                print("Error: Please enter a numeric grade.")
                continue

            collected[student_id] = f"{grade:.1f}"
            break

    # All grades validated
    # Putting the values to dictionary
    for student_id, grade_str in collected.items():
        students[student_id]["grades"].append(grade_str)

    enter()