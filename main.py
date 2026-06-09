from services.school_system import SchoolSystem

def display_menu():
    """Displays the main menu with all 11 available options to the user."""
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
    """Main function that runs the Student Course Registration System menu and handles user input."""
    # Create an instance of SchoolSystem which manages all students, courses, and registrations
    system = SchoolSystem()
    
    # Main loop continues until user selects option 0 to exit
    while True:
        # Display all menu options to the user
        display_menu()
        # Get user input and remove any extra whitespace
        choice = input("Choose an option: ").strip()

        # Option 1: Add a new student to the system
        if choice == "1":
            print("\n--- [1. Add Student] ---")
            # Collect student information from user input
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()
            phone = input("Enter Student Phone: ").strip()
            # Call backend function to add student with all four attributes
            system.add_student(student_id, name, email, phone)
            
        # Option 2: Display all students currently enrolled in the system
        elif choice == "2":
            print("\n--- [2. View Students] ---")
            # Call backend function to display all students
            system.display_all_students()
                    
        # Option 3: Search for a specific student by their ID
        elif choice == "3":
            print("\n--- [3. Search Student] ---")
            # Get the student ID to search for
            student_id = input("Enter Student ID to search: ").strip()
            # Call backend function to search and display the student
            system.search_student_by_id(student_id)
                
        # Option 4: Add a new course to the system
        elif choice == "4":
            print("\n--- [4. Add Course] ---")
            # Collect course information from user input
            course_id = input("Enter Course ID: ").strip()
            course_name = input("Enter Course Name: ").strip()
            # Collect trainer name for the course
            trainer_name = input("Enter Trainer Name: ").strip()
            capacity = input("Enter Maximum Capacity: ").strip()
            
            # Validate that capacity is a valid number before processing
            if capacity.isdigit():
                # Call backend function to add course with all four attributes
                system.add_course(course_id, course_name, trainer_name, int(capacity))
            else:
                print("Error: Capacity must be a whole number. Course not added.")
                
        # Option 5: Display all courses currently offered in the system
        elif choice == "5":
            print("\n--- [5. View Courses] ---")
            # Call backend function to display all courses
            system.display_all_courses()
                    
        # Option 6: Register a student to a course
        elif choice == "6":
            print("\n--- [6. Register Student to Course] ---")
            # Collect registration information from user
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()
            # Call backend function which validates and performs the registration
            system.register_student(student_id, course_id)
            
        # Option 7: Display all students registered in a specific course
        elif choice == "7":
            print("\n--- [7. View Students in a Course] ---")
            # Get the course ID from user
            course_id = input("Enter Course ID: ").strip()
            # Call backend function to display all students in this course
            system.display_students_in_course(course_id)
                    
        # Option 8: Display all courses a specific student is registered for
        elif choice == "8":
            print("\n--- [8. View Courses for a Student] ---")
            # Get the student ID from user
            student_id = input("Enter Student ID: ").strip()
            # Call backend function to display all courses for this student
            system.display_courses_for_student(student_id)
                    
        # Option 9: Save all system data to JSON files
        elif choice == "9":
            print("\n--- [9. Save Data] ---")
            # Call backend function to save students, courses, and registrations to JSON files
            system.save_to_json()
            
        # Option 10: Load all system data from JSON files
        elif choice == "10":
            print("\n--- [10. Load Data] ---")
            # Call backend function to load students, courses, and registrations from JSON files
            system.load_from_json()
            
        # Option 0: Exit the program
        elif choice == "0":
            print("\nThank you for using the Student Course Registration System. Goodbye!")
            # Break the loop to exit the program
            break
            
        # Handle invalid menu selections
        else:
            print("\nInvalid choice! Please select a valid number from the menu (0-10).")

if __name__ == "__main__":
    """Entry point for the Student Course Registration System."""
    main()
if __name__ == "__main__":
    main()