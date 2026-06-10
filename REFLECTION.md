# Project Reflection

## What was the hardest part of this project?

The hardest part of this project was designing the registration logic and ensuring that duplicate registrations were not allowed while also enforcing course capacity limits.

---

## Which classes did you create and why?

### Person

Created as a base class to store common information such as name, email, and phone number.

### Student

Created to represent students in the system. It inherits from Person and adds a student ID.

### Course

Created to represent courses offered by the training school.

### Registration

Created to represent the relationship between students and courses.

### SchoolSystem

Created to manage all business logic including student management, course management, registrations, validation, and file operations.

---

## How does your registration logic prevent duplicate registrations?

Before registering a student for a course, the system checks existing registration records. If the student is already registered for the selected course, the registration is rejected.

---

## How does your system check if a course is full?

The system counts the number of students registered for a course and compares that number with the course capacity. If the capacity has been reached, the registration is denied.

---

## What bugs did you face and how did you fix them?

One challenge involved handling invalid user input. I added validation checks and error handling to prevent the application from crashing when incorrect data was entered.

Another challenge involved duplicate records. This was solved by checking existing student IDs and course IDs before adding new records.

---

## Which part of the code would you improve if you had more time?

If I had more time, I would improve the user experience by adding an admin authentication system, reporting features, and a graphical user interface. I would also add more automated tests to improve reliability.

---

## What did you learn from this project?

This project improved my understanding of Object-Oriented Programming, inheritance, file handling, validation, and software design principles. It also helped me become more comfortable using Git and GitHub to manage project development.
