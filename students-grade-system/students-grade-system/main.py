from core_functions.grade_all_student import grade_all_student
from core_functions.grade_one_student import grade_one_student
from core_functions.grade_average import grade_average
from core_functions.modify_grades import modify_grades
from core_functions.add_grade import add_grade
from core_functions.add_student import add_student
from core_functions.delete_student import delete_student

from database.load_students import load_students
from database.save_students import save_exit

from ui.menu import menu

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