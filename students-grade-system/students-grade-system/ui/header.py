"""
It prints the header of the students' information.
"""

from utility.test_count import test_count


def header(students, format):

    if not students:
        return 0

    print(f"{'StudentID':<10} {'Student Name':<20}", end = " ")

    #sample_student = list(students.values())[0]
    max_test_count = test_count(students)

    if format == "test":
        for i in range(max_test_count):
            print("Test", i+1, sep = "", end = " ")
    elif format == "avg":
        print("Average")