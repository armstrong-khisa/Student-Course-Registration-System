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
    
    def add_student(self, student_id, name, email="", phone_number=""):
        """Creates a new Student object and adds it to the master list."""
        from models.student import Student
        
        # Create the instance with all required attributes
        new_student = Student(student_id, name, email, phone_number)
        self.students.append(new_student)
        print(f"\n[Success] Student '{name}' added successfully!")  
    
    def add_course(self, course_id, course_name, trainer_name, capacity):
        """Creates a new Course object and adds it to the master list."""
        from models.course import Course
        
        # Instantiate using your exact model parameters
        new_course = Course(course_id, course_name, trainer_name, capacity)
        self.courses.append(new_course)
        print(f"\n[Success] Course '{course_name}' added successfully!")
    
    def save_to_json(self):
        """Saves complete students, courses, and registrations into JSON files inside the data folder."""
        # 1. Convert Student objects (including Email and Phone) into dictionaries
        students_data = []
        for student in self.students:
            students_data.append({
                "student_id": student.student_id,
                "name": student.name,
                "email": student.email,
                "phone_number": student.phone_number
            })
            
        # 2. Convert Course objects (including Trainer) into dictionaries
        courses_data = []
        for course in self.courses:
            courses_data.append({
                "course_id": course.course_id,
                "course_name": course.course_name,
                "trainer_name": course.trainer_name,
                "capacity": course.capacity
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

    def load_from_json(self):
        """Loads students, courses, and registrations from JSON files inside the data folder."""
        # Import blueprints locally inside the method to prevent any circular import issues
        from models.student import Student
        from models.course import Course
        from models.registration import Registration
        
        # 1. Load Students
        try:
            with open("data/students.json", "r") as f:
                students_data = json.load(f)
                self.students = []  # Clear current memory list before loading
                for item in students_data:
                    # Create a formal Student object using all 4 attributes
                    student = Student(item["student_id"], item["name"], item["email"], item["phone_number"])
                    self.students.append(student)
            print("Loaded students successfully.")
        except FileNotFoundError:
            print("data/students.json not found. Starting with an empty student list.")
        except Exception as e:
            print(f"Error loading students: {e}")

        # 2. Load Courses
        try:
            with open("data/courses.json", "r") as f:
                courses_data = json.load(f)
                self.courses = []  # Clear current memory list before loading
                for item in courses_data:
                    # Create a formal Course object using all 4 attributes
                    course = Course(item["course_id"], item["course_name"], item["trainer_name"], item["capacity"])
                    self.courses.append(course)
            print("Loaded courses successfully.")
        except FileNotFoundError:
            print("data/courses.json not found. Starting with an empty course list.")
        except Exception as e:
            print(f"Error loading courses: {e}")

        # 3. Load Registrations
        try:
            with open("data/registrations.json", "r") as f:
                regs_data = json.load(f)
                self.registrations = []  # Clear current memory list before loading
                for item in regs_data:
                    # Create a formal Registration object mapping student_id and course_id
                    reg = Registration(item["student_id"], item["course_id"])
                    self.registrations.append(reg)
            print("Loaded registrations successfully.")
        except FileNotFoundError:
            print("data/registrations.json not found. Starting with empty registrations.")
        except Exception as e:
            print(f"Error loading registrations: {e}")

    def display_all_students(self):
        """Displays all students enrolled in the system with their complete information."""
        # Check if there are any students in the system before attempting to display
        if not self.students:
            print("No students registered in the system yet.")
        else:
            print("\nEnrolled Students:")
            # Loop through each student and display their information
            for student in self.students:
                print(student.display_info())
                # Print separator line for clean visual break between students
                print("-" * 30)

    def search_student_by_id(self, student_id):
        """
        Searches for a student by their ID and displays their information.
        This method handles both finding and displaying the result.
        """
        # Use the internal find method to locate the student
        student = self.find_student_by_id(student_id)
        # Check if student was found and display appropriate message
        if student:
            print(f"Found Student -> ID: {student.student_id} | Name: {student.name}")
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_courses(self):
        """Displays all courses offered in the system with their complete information."""
        # Check if there are any courses in the system before attempting to display
        if not self.courses:
            print("No courses offered in the system yet.")
        else:
            print("\nAvailable Courses:")
            # Loop through each course and display their information
            for course in self.courses:
                print(course.display_info())
                # Print separator line for clean visual break between courses
                print("-" * 30)

    def display_students_in_course(self, course_id):
        """
        Displays all students registered for a specific course.
        Parameters: course_id - the unique identifier of the course
        """
        # First verify that the course exists in the system
        course = self.find_course_by_id(course_id)
        if not course:
            print(f"Course with ID {course_id} does not exist.")
            return

        # Print header with course name
        print(f"\nStudents registered in {course.course_name}:")
        
        # Track whether we found any students in this course
        found_any = False
        
        # Loop through all registrations to find students in this course
        for reg in self.registrations:
            if reg.course_id == course_id:
                # Find the student object for this registration
                student = self.find_student_by_id(reg.student_id)
                if student:
                    print(f"- ID: {student.student_id} | Name: {student.name}")
                    found_any = True
        
        # Display message if no students were found
        if not found_any:
            print("No students are currently registered in this course.")

    def display_courses_for_student(self, student_id):
        """
        Displays all courses that a specific student is registered for.
        Parameters: student_id - the unique identifier of the student
        """
        # First verify that the student exists in the system
        student = self.find_student_by_id(student_id)
        if not student:
            print(f"Student with ID {student_id} does not exist.")
            return

        # Print header with student name
        print(f"\nCourses for {student.name}:")
        
        # Track whether we found any courses for this student
        found_any = False
        
        # Loop through all registrations to find courses for this student
        for reg in self.registrations:
            if reg.student_id == student_id:
                # Find the course object for this registration
                course = self.find_course_by_id(reg.course_id)
                if course:
                    print(f"- ID: {course.course_id} | Name: {course.course_name}")
                    found_any = True
        
        # Display message if no courses were found
        if not found_any:
            print("This student is not registered for any courses.")