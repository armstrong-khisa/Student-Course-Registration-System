from services.school_system import SchoolSystem
from models.student import Student
from models.course import Course

def display_menu():
    """Prints the official 11-option system menu to the terminal."""
    print("\n===== Student Course Registration System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("9. Save Data")
    print("10. Load Data")
    print("0. Exit")
    print("=============================================")

def main():
    # Instantiate our master system coordinator
    system = SchoolSystem()
    
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n--- [1. Add Student] ---")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            
            # Call the method from your school system backend
            system.add_student(student_id, name)
        elif choice == "2":
            print("\n--- [2. View Students] ---")
            if not system.students:
                print("No students registered in the system yet.")
            else:
                print("\nEnrolled Students:")
                for student in system.students:
                    print(f"ID: {student.student_id} | Name: {student.name}")
                    
        elif choice == "3":
            print("\n--- [3. Search Student] ---")
            student_id = input("Enter Student ID to search: ").strip()
            student = system.find_student_by_id(student_id)
            if student:
                print(f"Found Student -> ID: {student.student_id} | Name: {student.name}")
            else:
                print(f"Student with ID {student_id} not found.")
                
        elif choice == "4":
            print("\n--- [4. Add Course] ---")
            course_id = input("Enter Course ID: ").strip()
            course_name = input("Enter Course Name: ").strip()
            max_capacity = input("Enter Maximum Capacity: ").strip()
            
            # Simple conversion safeguard for capacity
            if max_capacity.isdigit():
                system.add_course(course_id, course_name, int(max_capacity))
            else:
                print("Error: Capacity must be a whole number. Course not added.")
                
        elif choice == "5":
            print("\n--- [5. View Courses] ---")
            if not system.courses:
                print("No courses offered in the system yet.")
            else:
                print("\nAvailable Courses:")
                for course in system.courses:
                    print(f"ID: {course.course_id} | Name: {course.course_name} | Capacity: {course.max_capacity}")
                    
        elif choice == "6":
            print("\n--- [6. Register Student to Course] ---")
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()
            
            # Executes our 4-check verification backend engine!
            system.register_student(student_id, course_id)
            
        elif choice == "7":
            print("\n--- [7. View Students in a Course] ---")
            course_id = input("Enter Course ID: ").strip()
            course = system.find_course_by_id(course_id)
            if not course:
                print(f"Course with ID {course_id} does not exist.")
            else:
                print(f"\nStudents registered in {course.course_name}:")
                found_any = False
                for reg in system.registrations:
                    if reg.course_id == course_id:
                        student = system.find_student_by_id(reg.student_id)
                        if student:
                            print(f"- ID: {student.student_id} | Name: {student.name}")
                            found_any = True
                if not found_any:
                    print("No students are currently registered in this course.")
                    
        elif choice == "8":
            print("\n--- [8. View Courses for a Student] ---")
            student_id = input("Enter Student ID: ").strip()
            student = system.find_student_by_id(student_id)
            if not student:
                print(f"Student with ID {student_id} does not exist.")
            else:
                print(f"\nCourses for {student.name}:")
                found_any = False
                for reg in system.registrations:
                    if reg.student_id == student_id:
                        course = system.find_course_by_id(reg.course_id)
                        if course:
                            print(f"- ID: {course.course_id} | Name: {course.course_name}")
                            found_any = True
                if not found_any:
                    print("This student is not registered for any courses.")
                    
        elif choice == "9":
            print("\n--- [9. Save Data] ---")
            # Placeholder for future file saving feature
            system.save_to_json()
            
        elif choice == "10":
            print("\n--- [10. Load Data] ---")
            # Placeholder for future file loading feature
            system.load_from_json()
            
        elif choice == "0":
            print("\nThank you for using the Student Course Registration System. Goodbye!")
            break  # Exits the interactive loop completely
            
        else:
            print("\nInvalid choice! Please select a valid number from the menu (0-10).")
if __name__ == "__main__":
    main()