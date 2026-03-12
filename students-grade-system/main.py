import sys

class StudentIDError(Exception):
    """Exception raised when user input a Student ID which is already in the Dataset during addition or missing during deletion."""
    pass


def test_count(students):
    if not students:
        return 0
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

                student_grades = grades.split()

                students[student_id.strip()] = {
                    "name" : student_name.strip(),
                    "grades" : student_grades}


    except FileNotFoundError:
        print(f"File not Found")

    return students


def save_exit(students, FILE_NAME):                             #Option 8

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

    if not students:
        return 0

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
        total = 0

        if len(student_info["grades"]) == 0:
            print(f"{'N/A':>8}")
            return

        for score in student_info["grades"]:
            count += 1
            total += float(score)
        print(f"{total/count:.1f}")


def grade_all_student(students):                                #Option 1

    if not students:                            # students == ""
        print("No dataset for Students")
        return

    #print("StudentID", "Student Name", end = " ")
    header(students, "test")
    print("\n")

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "test")

    enter()


def grade_one_student(students):                                #Option 2

    student_id = input("Enter studentID: ").strip()

    if student_id in students:
        header(students, "test")
        student_info = students[student_id]
        print()
        database_print(student_id, student_info, "test")

    else:
        print("Error: Invalid student ID")

    enter()


def grade_average(students):                                    #Option 3

    header(students, "avg")
    print()

    for student_id, student_info in students.items():
        database_print(student_id, student_info, "avg")

    enter()


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


def add_student(students):                                      #Option 6

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students.keys():
            raise StudentIDError

        else:
            student_name = input("Enter Student Name: ").strip()
            student_grades = []
            for i in range(test_count(students)):

                while True:
                    try:
                        grade = float(input(f"Enter grade for test#{i+1}: "))
                    except ValueError:
                        print("Enter a valid grade")
                        continue

                    if 0 <= grade <= 100:
                        break

                    print("Error: Grade must be between 0 and 100. Please try again.")

                student_grades.append(f"{grade:.1f}")

            students[student_id] = {"name": student_name, "grades": student_grades}

    except StudentIDError:
        print("Student ID already exists")

    enter()


def delete_student(students):                                   #Option 7
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

