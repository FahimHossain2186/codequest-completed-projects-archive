import os

'''
This function loads student information from a file and returns a dictionary of students.
The function takes in the file name as an argument and reads the file line by line.
Then it splits each line into student ID, student name, and student grades using the '#' as separator.
The student information is stored in a dictionary where the key is the student ID and 
the value is another dictionary containing the student's name and a list of their grades.
'''

'''
The style we used for dictionary is:

students = {
    "student_id1": {
        "name": "Student Name 1",
        "grades": ["85.0", "90.0", "78.0"]          # List of grades as strings
    }
}
'''

def load_students(FILE_NAME):

    students = {}
    FILE_NAME = os.path.join(os.path.dirname(__file__), "data", FILE_NAME)      # Get the absolute path to the file in the data directory

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

        #print(students)

    except FileNotFoundError:
        print(f"File not Found")

    return students