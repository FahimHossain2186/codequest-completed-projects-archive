import os

def save_exit(students, FILE_NAME):                             #Option 8

    FILE_NAME = os.path.join(os.path.dirname(__file__), "data", FILE_NAME)

    try:
        with open(FILE_NAME, "w") as file:

            for student_id, student_info in students.items():
                name = student_info["name"]
                '''
                student_info["grades"] --> list of grades
                " ".join --> " " + grade1 + " " + grade2 + ... 
                '''
                grades_string = " ".join(student_info["grades"])

                #91007# Ahmad Said# 50.0 78.5 73.2
                file.write(f"{student_id}# {name}# {grades_string}\n")


    except Exception as e:
        print(f"Error saving file: {e}")
