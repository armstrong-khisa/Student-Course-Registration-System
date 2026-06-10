# Student Course Registration System

## Project Overview

The Student Course Registration System is a command-line Python application that helps a training school manage students, courses, and course registrations.

The system allows an administrator to:

* Add students
* View students
* Search for students
* Add courses
* View courses
* Register students for courses
* View students registered in a course
* View courses registered by a student
* Save data to files
* Load data from files

The project was developed using Object-Oriented Programming (OOP) principles including classes, inheritance, encapsulation, file handling, and error handling.

---

## Features Implemented

### Student Management

* Add new students
* View all students
* Search students by ID or name
* Prevent duplicate student IDs

### Course Management

* Add new courses
* View all courses
* Prevent duplicate course IDs

### Registration Management

* Register students to courses
* Prevent duplicate registrations
* Enforce course capacity limits
* View students registered in a course
* View courses registered by a student

### Data Persistence

* Save data using JSON files
* Load saved data when the application starts

---

## Project Structure

student-course-registration/

├── main.py

├── models/

│ ├── person.py

│ ├── student.py

│ ├── course.py

│ └── registration.py

├── services/

│ └── school_system.py

├── data/

│ ├── students.json

│ ├── courses.json

│ └── registrations.json

├── README.md

└── REFLECTION.md

---

## Classes Used

### Person

Base class containing common attributes:

* Name
* Email
* Phone Number

### Student

Inherits from Person and adds:

* Student ID

### Course

Represents a course and stores:

* Course ID
* Course Name
* Trainer Name
* Capacity

### Registration

Represents the relationship between a student and a course.

### SchoolSystem

Manages students, courses, registrations, validation, and application logic.

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* JSON File Handling
* Git & GitHub

---

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate into the project directory

```bash
cd Student-Course-Registration-System
```

3. Run the application

```bash
python3 main.py
```

---

## Learning Outcomes

Through this project I practiced:

* Classes and Objects
* Inheritance
* Functions
* Lists and Dictionaries
* File Handling
* Error Handling
* Git and GitHub Version Control
* Command-Line Application Development

---

## Author

Armstrong Khisa
