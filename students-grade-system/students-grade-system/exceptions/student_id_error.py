class StudentIDError(Exception):
    """Exception raised when user input a Student ID which is already in the Dataset during addition or missing during deletion."""
    pass