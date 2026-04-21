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
        "grades": ["grade1", "grade2", "grade3", ...]          # List of grades as strings
    }
}
'''

def load_students(FILE_NAME):

    students = {}

    # Get the absolute path to the file in the data directory
    
    '''                                        
    __file__ --> the path of the current file (load_students.py)
    os.path.dirname(__file__) --> the directory of the current file (database)
    os.path.join(os.path.dirname(__file__), "data", FILE_NAME) --> directory of the current file/data/"FILE_NAME" 

    This ensures that the file is correctly located regardless of where the script is run from, 
    as it constructs the path relative to the location of the current script.
    '''

    # Using raw string for docstrings to avoid SyntaxWarning: invalid escape sequence '\s'
    r"""
    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.join(os.path.dirname(__file__), "data", FILE_NAME))

    The output will be something like this:
    ...\students-grade-system\database\load_students.py
    ...\students-grade-system\database
    ...\students-grade-system\database\data\grades.txt
    """
    

    FILE_NAME = os.path.join(os.path.dirname(__file__), "data", FILE_NAME)      


    try:
        with open(FILE_NAME, "r") as file:

            """
            Lets consider the first line of the file is:
            91007# Ahmad Said# 50.0 78.5 73.2

            line.strip() --> "91007# Ahmad Said# 50.0 78.5 73.2"
            line.count("#") --> 2 (there are 2 '#' in the line)
            line.split("#") --> ["91007", " Ahmad Said", " 50.0 78.5 73.2"]

            student_id, student_name, student_grades = line.split("#") --> 
            student_id = "91007", student_name = " Ahmad Said", student_grades = " 50.0 78.5 73.2"

            students[student_id.strip()] --> students["91007"] = {
                "name" : student_name.strip(), --> "Ahmad Said"
                "grades" : student_grades.split()} --> ["50.0", "78.5", "73.2"]
                }
            
            # After processing the first line, the students dictionary will look like this:
            students = {
                "91007": {
                    "name": "Ahmad Said",
                    "grades": ["50.0", "78.5", "73.2"]
                }
            }

            Here 91007 is the key to initial dictionary and the value is another dictionary that is {"name": "Ahmad Said", "grades": ["50.0", "78.5", "73.2"]}
            In the inner dictionary, "name" is the key and "Ahmad Said" is the value, 
            and "grades" is the key and ["50.0", "78.5", "73.2"] is the value which is a list of strings.
            """

            for line in file:
                line = line.strip()
                if not line or line.count("#") != 2:
                    continue

                student_id, student_name, student_grades = line.split("#")

                students[student_id.strip()] = {
                    "name" : student_name.strip(),
                    "grades" : student_grades.split()
                    }

        #print(students)

    except FileNotFoundError:
        print(f"File not Found")

    return students