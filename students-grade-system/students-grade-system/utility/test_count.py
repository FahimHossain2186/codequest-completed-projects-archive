def test_count(students):
    if not students:
        return 0
    sample_student = list(students.values())[0]
    return len(sample_student["grades"])