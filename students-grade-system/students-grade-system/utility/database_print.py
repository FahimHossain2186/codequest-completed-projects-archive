"""
This module contains the function to print the students' information in a formatted way. 
The function takes in the student ID, student information, and the format to print the information. 
The function prints the student ID, name, and either the test scores or the average score depending on the format specified.
"""

def database_print(student_id, student_info, format):

    """
    The Student ID consists of 5 digits, so using (9-len(student_id)) 
    we calculate the number of spaces needed to align the student ID to the right.
    The student name is left-aligned with a width of 20 characters.

    """

    print(f"{' ' * (9-len(student_id))}{student_id}  {student_info['name']:<20}", end = " ")

    if format == "test":

        for score in student_info["grades"]:
            # Each score is formatted with 5 characters as the chracter count for (Test1, Test2, Test3) is 5 
            print(f"{score:<5}", end = " ")         
        
        print()
    
    elif format == "avg":
        
        count = 0
        total = 0

        if len(student_info["grades"]) == 0:
            print(f"{'N/A'}")
            return

        for score in student_info["grades"]:
            count += 1
            total += float(score)
        print(f"{total/count:.1f}")