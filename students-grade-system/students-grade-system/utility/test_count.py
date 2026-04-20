"""
This module contains the function to count the number of grades for a student. 
The function takes in the students' information and returns the number of grades for a sample student. 
"""

def test_count(students):
    if not students:
        return 0
    sample_student = list(students.values())[0]
    return len(sample_student["grades"])