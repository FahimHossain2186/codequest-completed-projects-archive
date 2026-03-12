import sys

class StudentIDError(Exception):
    """Exception raised when user input a Student ID which is already in the Dataset during addition or missing during deletion."""
    pass


def test_count(students):
    sample_student = list(students.values())[0]
    return len(sample_student["grades"])


def load_students(FILE_NAME):

    students = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                student_id, student_name, grades = line.split("#")
                student_name = student_name.strip()
                if grades == "":
                    continue

                #print(student_grades) --> For Checking
                student_grades = grades.split()

                students[student_id.strip()] = {
                    "name" : student_name.strip(),
                    "grades" : student_grades}

            '''
            Check Purpose:

                for student_id, student_info in students.items():
                    print(student_id, student_info)
                    print(student_id, student_info[0])
                    print(student_id, student_info[1])
                    print(student_id, student_info[1][0])
            '''

    except FileNotFoundError:
        print(f"File not Found")

    return students


def save_exit(students, FILE_NAME):

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

        sys.exit()

    except Exception as e:
        print(f"Error saving file: {e}")


def enter():
    input("\nPress Enter key to continue . . .")
    return


def header(students, format):

    print(f"{'StudentID':<10} {'Student Name':<20}", end = " ")

    sample_student = list(students.values())[0]

    if format == "test":
        for i in range(len(sample_student["grades"])):
            print("Test", i+1, sep = "", end = " ")
    elif format == "avg":
        print("Average")


def database_print(student_id, student_info, format):

    print(f"{' ' * (9-len(student_id))}{student_id}  {student_info['name']:<20}", end = " ")

    if format == "test":
        for score in student_info["grades"]:
            print(f"{score:<5}", end = " ")
        print()
    elif format == "avg":
        count = 0
        sum = 0
        for score in student_info["grades"]:
            count += 1
            sum += float(score)
        print(f"{sum/count:.1f}")


def grade_all_student(students):

    if not students:                            # students == ""
        print("No dataset for Students")
        return

    #print("StudentID", "Student Name", end = " ")
    header(students, "test")
    print("\n")

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "test")

    enter()


def grade_one_student(students):

    student_id = input("Enter studentID: ").strip()

    if student_id in students:
        header(students, "test")
        student_info = students[student_id]
        print()
        database_print(student_id, student_info, "test")

    else:
        print("Error: Invalid student ID")

    enter()


def grade_average(students):

    header(students, "avg")
    print()

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "avg")

    enter()


def modify_grades(students):

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students:

            quiz_no = int(input("Please enter quiz number to modify: ").strip()) - 1
            student_info = students[student_id]

            if 0 <= quiz_no < len(student_info["grades"]):

                changed_grade = float(input(f"Please enter new quiz {quiz_no+1} grade: "))

                print("Before grade modification: ", end = "")
                database_print(student_id, student_info, "test")

                student_info["grades"][quiz_no] = f"{changed_grade:.1f}"
                print("After grade modification:  ", end = "")
                database_print(student_id, student_info, "test")

            else:
                print("Error: Invalid quiz number")
        else:
            print("Error: Invalid student ID")

    except ValueError:
        print("Error: Invalid quiz number")

    enter()


def add_grade(students):

    test_number = test_count(students)
    print(f"Please enter test grades for Test#{test_number+1}\n")

    for student_id, student_info in students.items():
        test_number = float(input(f"Please enter grade for student : {student_id}\n").strip())
        student_info["grades"].append(f"{test_number:.1f}")

    enter()


def add_student(students):

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students.keys():
            raise StudentIDError

        else:
            student_name = input("Enter Student Name: ").strip()
            student_grades = []
            for i in range(test_count(students)):
                grade = float(input(f"Enter grade for test#{i+1}: "))

                student_grades.append(f"{grade:.1f}")

            students[student_id] = {"name": student_name, "grades": student_grades}

    except StudentIDError as e:
        print("Student ID already exists")

    enter()


def delete_student(students):
    try:
        student_id = input("Enter studentID: ").strip()

        if not student_id in students.keys():
            raise StudentIDError

        else:
            students.pop(student_id)

    except StudentIDError as e:
        print("Student ID doesn't exist")

    enter()


def menu():
    print("\n"  + "-" * 60)
    print(" " * 14 + "Student Grade Management System")
    print("-" * 60)
    print("1. Display Grade Info for all students",
          "2. Display Grade Info for a particular student",
          "3. Display tests average for all students",
          "4. Modify a particular test grade for a particular student",
          "5. Add test grades for a particular test for all students",
          "6. Add a new Student",
          "7. Delete a student",
          "8. Save and Exit", sep="\n")
    print("-" * 60)


def main():

    """
    Program starts here
    """
    FILE_NAME = "grades.txt"
    students = load_students(FILE_NAME)

    option = 1

    while option != 8:
        menu()
        try:
            option = int(input("\nPlease select your choice: "))

            print()

            if not(8 >= option >= 1):
                raise ValueError

            match option:
                case 1:
                    grade_all_student(students)
                case 2:
                    grade_one_student(students)
                case 3:
                    grade_average(students)
                case 4:
                    modify_grades(students)
                case 5:
                    add_grade(students)
                case 6:
                    add_student(students)
                case 7:
                    delete_student(students)
                case 8:
                    save_exit(students, FILE_NAME)

        except ValueError:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()

