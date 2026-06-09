import re

class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        if not self.validate_course_id(course_id):
            raise ValueError(f"Invalid Course ID: {course_id}")
        if not self.validate_course_name(course_name):
            raise ValueError(f"Invalid Course Name: {course_name}")
        if not self.validate_trainer_name(trainer_name):
            raise ValueError(f"Invalid Trainer Name: {trainer_name}")
        if not self.validate_capacity(capacity):
            raise ValueError(f"Invalid Capacity: {capacity}")
        
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = capacity

    @staticmethod
    def validate_course_id(course_id):
        pattern = r'^[A-Za-z0-9_-]{3,20}$'
        return re.match(pattern, str(course_id)) is not None

    @staticmethod
    def validate_course_name(course_name):
        pattern = r'^[A-Za-z0-9\s]{3,100}$'
        return re.match(pattern, str(course_name)) is not None

    @staticmethod
    def validate_trainer_name(trainer_name):
        pattern = r'^[A-Za-z\s]{2,50}$'
        return re.match(pattern, str(trainer_name)) is not None

    @staticmethod
    def validate_capacity(capacity):
        if isinstance(capacity, int):
            return capacity > 0
        pattern = r'^[0-9]+$'
        if re.match(pattern, str(capacity)):
            return int(capacity) > 0
        return False

    def display_info(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Trainer: {self.trainer_name}\n"
            f"Capacity: {self.capacity} students"
        )