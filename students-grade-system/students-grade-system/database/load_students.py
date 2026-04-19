import os


def load_students(FILE_NAME):

    students = {}
    FILE_NAME = os.path.join(os.path.dirname(__file__), "data", FILE_NAME)

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.count("#") != 2:
                    continue

                student_id, student_name, student_grades = line.split("#")

                students[student_id.strip()] = {
                    "name" : student_name.strip(),
                    "grades" : student_grades.split()}


    except FileNotFoundError:
        print(f"File not Found")

    return students