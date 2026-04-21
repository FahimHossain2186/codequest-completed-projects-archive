"""
This module contains the function to count the number of grades for a student. 
The function takes in the students' information and returns the number of grades for a sample student. 
"""

def test_count(students):
    if not students:
        return 0
    return max(len(student_info["grades"]) for student_info in students.values())