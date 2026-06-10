import json

from models.registration import Registration


# Central class responsible for managing students, courses, and registrations
class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

    # Search for a student using their unique ID
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # Search for a course using its unique ID
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    # Count how many students are currently enrolled in a course
    def count_students_in_course(self, course_id):
        count = 0
        for reg in self.registrations:
            if reg.course_id == course_id:
                count += 1
        return count

    def register_student(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        if not student:
            print(f"Registration failed: Student with ID {student_id} does not exist.")
            return False

        course = self.find_course_by_id(course_id)
        if not course:
            print(f"Course with ID {course_id} does not exist.")
            return False

        # Prevent duplicate registrations
        for reg in self.registrations:
            if reg.student_id == student_id and reg.course_id == course_id:
                print(f"Registration failed: {student.name} is already registered for {course.course_name}.")
                return False

        # Ensure the course has not reached its capacity
        current_count = self.count_students_in_course(course_id)
        if current_count >= course.capacity:
            print(f"Registration failed: {course.course_name} is full (capacity {course.capacity}).")
            return False

        # Create a new registration record
        new_reg = Registration(student_id, course_id)
        self.registrations.append(new_reg)

        print(f"Success: {student.name} has been registered for {course.course_name}!")
        return True

    def add_student(self, student_id, name, email="", phone_number=""):
        from models.student import Student

        try:
            new_student = Student(student_id, name, email, phone_number)
            self.students.append(new_student)
            print(f"\n[Success] Student '{name}' added successfully!")
        except ValueError as e:
            print(f"\n[Error] {e}")

    def add_course(self, course_id, course_name, trainer_name, capacity):
        from models.course import Course

        try:
            new_course = Course(course_id, course_name, trainer_name, capacity)
            self.courses.append(new_course)
            print(f"\n[Success] Course '{course_name}' added successfully!")
        except ValueError as e:
            print(f"\n[Error] {e}")

    # Save all system data to JSON files for persistence
    def save_to_json(self):
        students_data = []
        for student in self.students:
            students_data.append({
                "student_id": student.student_id,
                "name": student.name,
                "email": student.email,
                "phone_number": student.phone_number
            })

        courses_data = []
        for course in self.courses:
            courses_data.append({
                "course_id": course.course_id,
                "course_name": course.course_name,
                "trainer_name": course.trainer_name,
                "capacity": course.capacity
            })

        regs_data = []
        for reg in self.registrations:
            regs_data.append({
                "student_id": reg.student_id,
                "course_id": reg.course_id
            })

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

    # Load previously saved data when the application starts
    def load_from_json(self):
        from models.student import Student
        from models.course import Course
        from models.registration import Registration

        try:
            with open("data/students.json", "r") as f:
                students_data = json.load(f)
                self.students = []

                # Recreate Student objects from stored JSON data
                for item in students_data:
                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["email"],
                        item["phone_number"]
                    )
                    self.students.append(student)

            print("Loaded students successfully.")

        except FileNotFoundError:
            print("data/students.json not found. Starting with an empty student list.")
        except Exception as e:
            print(f"Error loading students: {e}")

        try:
            with open("data/courses.json", "r") as f:
                courses_data = json.load(f)
                self.courses = []

                for item in courses_data:
                    course = Course(
                        item["course_id"],
                        item["course_name"],
                        item["trainer_name"],
                        item["capacity"]
                    )
                    self.courses.append(course)

            print("Loaded courses successfully.")

        except FileNotFoundError:
            print("data/courses.json not found. Starting with an empty course list.")
        except Exception as e:
            print(f"Error loading courses: {e}")

        try:
            with open("data/registrations.json", "r") as f:
                regs_data = json.load(f)
                self.registrations = []

                for item in regs_data:
                    reg = Registration(
                        item["student_id"],
                        item["course_id"]
                    )
                    self.registrations.append(reg)

            print("Loaded registrations successfully.")

        except FileNotFoundError:
            print("data/registrations.json not found. Starting with empty registrations.")
        except Exception as e:
            print(f"Error loading registrations: {e}")

    # Display all students currently stored in the system
    def display_all_students(self):
        if not self.students:
            print("No students registered in the system yet.")
        else:
            print("\nEnrolled Students:")
            for student in self.students:
                print(student.display_info())
                print("-" * 30)

    def search_student_by_id(self, student_id):
        student = self.find_student_by_id(student_id)

        if student:
            print(f"Found Student -> ID: {student.student_id} | Name: {student.name}")
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_courses(self):
        if not self.courses:
            print("No courses offered in the system yet.")
        else:
            print("\nAvailable Courses:")
            for course in self.courses:
                print(course.display_info())
                print("-" * 30)

    # Show all students registered in a selected course
    def display_students_in_course(self, course_id):
        course = self.find_course_by_id(course_id)

        if not course:
            print(f"Course with ID {course_id} does not exist.")
            return

        print(f"\nStudents registered in {course.course_name}:")

        found_any = False

        for reg in self.registrations:
            if reg.course_id == course_id:
                student = self.find_student_by_id(reg.student_id)

                if student:
                    print(f"- ID: {student.student_id} | Name: {student.name}")
                    found_any = True

        if not found_any:
            print("No students are currently registered in this course.")

    # Show all courses a particular student is taking
    def display_courses_for_student(self, student_id):
        student = self.find_student_by_id(student_id)

        if not student:
            print(f"Student with ID {student_id} does not exist.")
            return

        print(f"\nCourses for {student.name}:")

        found_any = False

        for reg in self.registrations:
            if reg.student_id == student_id:
                course = self.find_course_by_id(reg.course_id)

                if course:
                    print(f"- ID: {course.course_id} | Name: {course.course_name}")
                    found_any = True

        if not found_any:
            print("This student is not registered for any courses.")