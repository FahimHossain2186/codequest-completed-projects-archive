def load_students():

    students = {}

    try:
        with open("grades.txt", "r") as file:
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

                for key, value in students.items():
                    print(key, value)
                    print(key, value[0])
                    print(key, value[1])
                    print(key, value[1][0])
            '''

    except FileNotFoundError:
        print(f"File not Found")

    return students


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


def database_print(key, value, format):

    print(f"{' ' * (9-len(key))}{key}  {value['name']:<20}", end = " ")

    if format == "test":
        for score in value["grades"]:
            print(f"{score:<5}", end = " ")
        print()
    elif format == "avg":
        count = 0
        sum = 0
        for score in value["grades"]:
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

    for key, value in students.items():
        database_print(key, value, "test")

    enter()


def grade_one_student(students):

    student_id = input("Enter studentID: ").strip()

    if student_id in students:
        header(students, "test")
        value = students[student_id]
        print()
        database_print(student_id, value, "test")

    else:
        print("Error: Invalid student ID")

    enter()


def grade_average(students):

    header(students, "avg")
    print()

    for key, value in students.items():
        database_print(key, value, "avg")

    enter()


def modify_grades(students):

    try:
        student_id = input("Enter studentID: ").strip()

        if student_id in students:

            quiz_no = int(input("Please enter quiz number to modify: ").strip()) - 1
            value = students[student_id]

            if 0 <= quiz_no < len(value["grades"]):

                changed_grade = input(f"Please enter new quiz {quiz_no} grade: ")

                print("Before grade modification: ", end = "")
                database_print(student_id, value, "test")

                value["grades"][quiz_no] = changed_grade
                print("After grade modification:  ", end = "")
                database_print(student_id, value, "test")

            else:
                print("Error: Invalid quiz number")
        else:
            print("Error: Invalid student ID")

    except ValueError:
        print("Error: Invalid quiz number")

    enter()


def add_grade(students):
    ...


def add_student(students):
    ...


def delete_student(students):
    ...


def save_exit(students):
    ...


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

    students = load_students()

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
                    ...

        except ValueError:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()

