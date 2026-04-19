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