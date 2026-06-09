from models.registration import Registration

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
            return None

    def register_student(self , student_id, course_id):
        student = self.find_student_by_id(student_id)
        if not student:
            print(f"Registration failed: Student with ID {student_id} does not exist.")
            return False

        course = self.find_course_by_id(course_id)
        if not course:
            print(f"Course with ID {course_id} does not exist.")
            return False

        for reg in self.registrations:
            if reg.student_id == student_id and reg.course_id == course_id:
                print(f"Registration failed: {student.name} is already registered for {course.course_name}.")
                return False

        new_reg = Registration(student_id, course_id)
        self.registrations.append(new_reg)
        print(f"Success: {student.name} has been registered for {course.course_name}!")
        return True