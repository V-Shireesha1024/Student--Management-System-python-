students = []


def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    print("\n--- Student Details ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("Roll No :", student["roll_no"])
        print("Name    :", student["name"])
        print("Course  :", student["course"])
        print("Marks   :", student["marks"])
        print("------------------------")


def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found!")
            print("Name   :", student["name"])
            print("Course :", student["course"])
            print("Marks  :", student["marks"])
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = float(input("Enter new marks: "))

            print("Student details updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
