import re
from models.person import Person


# Student inherits common personal details from the Person class
class Student(Person):
    def __init__(self, student_id, name, email, phone_number):

        # Validate student information before creating the object
        if not self.validate_student_id(student_id):
            raise ValueError(f"Invalid Student ID: {student_id}")

        if not self.validate_name(name):
            raise ValueError(f"Invalid Name: {name}")

        if not self.validate_email(email):
            raise ValueError(f"Invalid Email: {email}")

        if not self.validate_phone(phone_number):
            raise ValueError(f"Invalid Phone: {phone_number}")

        # Initialize inherited attributes from the Person class
        super().__init__(name, email, phone_number)

        self.student_id = student_id

    # Student IDs must follow a consistent format
    @staticmethod
    def validate_student_id(student_id):
        pattern = r'^[A-Za-z0-9_-]{3,20}$'
        return re.match(pattern, student_id) is not None

    # Names should contain letters and spaces only
    @staticmethod
    def validate_name(name):
        pattern = r'^[A-Za-z\s]{2,50}$'
        return re.match(pattern, name) is not None

    # Validate email using a basic email pattern
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    # Allow digits, spaces, dashes and brackets in phone numbers
    @staticmethod
    def validate_phone(phone_number):
        pattern = r'^[0-9\s\-()]{7,15}$'
        return re.match(pattern, phone_number) is not None

    # Returns student details in a readable format
    def display_info(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone_number}"
        )