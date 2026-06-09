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
    def register_student(self , student_id, course_id):
        student = self.find_student_by_id(student_id)
        if not student:
            print(f"Registration failed: Student with ID {student_id} does not exist.")
            return False
