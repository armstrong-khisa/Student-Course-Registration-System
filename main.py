from services.school_system import SchoolSystem
from models.student import Student
from models.course import Course

# --- REUSABLE INPUT VALIDATION CONTROLLER ---
def get_validated_input(prompt, validation_fn, error_requirements):
    """
    Prompts the user quietly. 
    Only prints the formatting requirements if the user enters invalid data.
    """
    while True:
        user_input = input(prompt).strip()
        
        if user_input.lower() == 'q':
            print("\n[Operation Cancelled] Returning to main menu...")
            return None
            
        if validation_fn(user_input):
            return user_input
        else:
            # Only display instructions on a failed validation attempt!
            print(f"\n❌ Invalid Input. Requirements: {error_requirements}")
            print("Please try again or type 'q' to cancel.\n")

def main():
    system = SchoolSystem()
    
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n--- [1. Add Student] ---")
            print("(Note: Type 'q' at any prompt to cancel and return to main menu)")
            
            student_id = get_validated_input(
                "Enter Student ID: ", 
                Student.validate_student_id, 
                "Alphanumeric with underscores or dashes (3-20 characters)."
            )
            if student_id is None: continue
            
            name = get_validated_input(
                "Enter Student Name: ", 
                Student.validate_name, 
                "Letters and spaces only (2-50 characters)."
            )
            if name is None: continue
            
            email = get_validated_input(
                "Enter Student Email: ", 
                Student.validate_email, 
                "Valid email format (e.g., user@domain.com)."
            )
            if email is None: continue
            
            phone = get_validated_input(
                "Enter Student Phone: ", 
                Student.validate_phone, 
                "Digits, spaces, dashes, parentheses (7-15 characters)."
            )
            if phone is None: continue
            
            system.add_student(student_id, name, email, phone)
            
        elif choice == "2":
            print("\n--- [2. View Students] ---")
            system.display_all_students()
                    
        elif choice == "3":
            print("\n--- [3. Search Student] ---")
            student_id = input("Enter Student ID to search: ").strip()
            system.search_student_by_id(student_id)
                
        elif choice == "4":
            print("\n--- [4. Add Course] ---")
            print("(Note: Type 'q' at any prompt to cancel and return to main menu)")
            
            course_id = get_validated_input(
                "Enter Course ID: ", 
                Course.validate_course_id, 
                "Alphanumeric with underscores or dashes (3-20 characters)."
            )
            if course_id is None: continue
            
            course_name = get_validated_input(
                "Enter Course Name: ", 
                Course.validate_course_name, 
                "Alphanumeric and spaces (3-100 characters)."
            )
            if course_name is None: continue
            
            trainer_name = get_validated_input(
                "Enter Trainer Name: ", 
                Course.validate_trainer_name, 
                "Letters and spaces only (2-50 characters)."
            )
            if trainer_name is None: continue
            
            capacity = get_validated_input(
                "Enter Maximum Capacity: ", 
                Course.validate_capacity, 
                "Positive whole number greater than 0."
            )
            if capacity is None: continue
            
            # Safe to pass to system and cast capacity safely to an int
            system.add_course(course_id, course_name, trainer_name, int(capacity))
                
        elif choice == "5":
            print("\n--- [5. View Courses] ---")
            system.display_all_courses()
                    
        elif choice == "6":
            print("\n--- [6. Register Student to Course] ---")
            student_id = input("Enter Student ID: ").strip()
            course_id = input("Enter Course ID: ").strip()
            system.register_student(student_id, course_id)
            
        elif choice == "7":
            print("\n--- [7. View Students in a Course] ---")
            course_id = input("Enter Course ID: ").strip()
            system.display_students_in_course(course_id)
                    
        elif choice == "8":
            print("\n--- [8. View Courses for a Student] ---")
            student_id = input("Enter Student ID: ").strip()
            system.display_courses_for_student(student_id)
                    
        elif choice == "9":
            print("\n--- [9. Save Data] ---")
            system.save_to_json()
            
        elif choice == "10":
            print("\n--- [10. Load Data] ---")
            system.load_from_json()
            
        elif choice == "0":
            print("\nThank you for using the Student Course Registration System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please select a valid number from the menu (0-10).")

def display_menu():
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

if __name__ == "__main__":
    main()