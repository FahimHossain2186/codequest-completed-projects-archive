"""
This module contains the function to display the main menu of the student grade management system.
"""

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