def add_student(students):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!\n")


def display_students(students):
    if not students:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for name, marks in students.items():
            print(f"{name} : {marks}")
        print()


def find_topper(students):
    if students:
        topper = max(students, key=students.get)
        print(f"Topper: {topper} with {students[topper]} marks\n")
    else:
        print("No records available.\n")


students = {}

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        find_topper(students)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!\n")
