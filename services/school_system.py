import json

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
    
    def save_to_json(self):
        """Saves complete students, courses, and registrations into JSON files inside the data folder."""
        # 1. Convert Student objects (including Email and Phone) into dictionaries
        students_data = []
        for student in self.students:
            students_data.append({
                "student_id": student.student_id,
                "name": student.name,
                "email": student.email,
                "phone": student.phone
            })
            
        # 2. Convert Course objects (including Trainer) into dictionaries
        courses_data = []
        for course in self.courses:
            courses_data.append({
                "course_id": course.course_id,
                "course_name": course.course_name,
                "trainer": course.trainer,
                "max_capacity": course.max_capacity
            })
            
        # 3. Convert Registration objects into dictionaries
        regs_data = []
        for reg in self.registrations:
            regs_data.append({
                "student_id": reg.student_id,
                "course_id": reg.course_id
            })
            
        # 4. Write data to JSON files
        try:
            with open("data/students.json", "w") as f:
                json.dump(students_data, f, indent=4)
                
            with open("data/courses.json", "w") as f:
                json.dump(courses_data, f, indent=4)
                
            with open("data/registrations.json", "w") as f:
                json.dump(regs_data, f, indent=4)
                
            print("\n[Success] All comprehensive data saved to the data/ directory!")
            
        except Exception as e:
            print(f"\n[Error] Failed to save data: {e}")