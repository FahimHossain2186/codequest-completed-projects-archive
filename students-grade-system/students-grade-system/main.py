import sys

from core_functions.grade_all_student import grade_all_student
from core_functions.grade_one_student import grade_one_student
from core_functions.grade_average import grade_average
from core_functions.modify_grades import modify_grades
from core_functions.add_grade import add_grade
from core_functions.add_student import add_student
from core_functions.delete_student import delete_student

from database.load_students import load_students
from database.save_students import save_students

from ui.menu import menu

def main():

    """
    In the main function, we load the students from the file using the load_students function, 
    and then we display the menu to the user. The user can select an option from the menu, 
    and then we call the corresponding function to perform the action. If the user selects option 8, 
    we save the students to the file and exit the program.
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
                    save_students(students, FILE_NAME)
                    sys.exit()

        except ValueError:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()