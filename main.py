from services.school_system import SchoolSystem

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

def main():
    system = SchoolSystem()
    
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n--- [1. Add Student] ---")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()
            phone = input("Enter Student Phone: ").strip()
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
            course_id = input("Enter Course ID: ").strip()
            course_name = input("Enter Course Name: ").strip()
            trainer_name = input("Enter Trainer Name: ").strip()
            capacity = input("Enter Maximum Capacity: ").strip()
            
            if capacity.isdigit():
                system.add_course(course_id, course_name, trainer_name, int(capacity))
            else:
                print("Error: Capacity must be a whole number. Course not added.")
                
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

if __name__ == "__main__":
    main()