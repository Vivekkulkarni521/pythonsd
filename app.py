# Student Management System

students = {
    "Vivek": 90,
    "Rahul": 85,
    "Anita": 95,
    "Priya": 88,
    "Karan": 92
}

print("===================================")
print("     STUDENT MANAGEMENT SYSTEM")
print("===================================\n")

print("Student Records:")
for name, marks in students.items():
    print(f"{name} : {marks}")

# Calculate average marks
average_marks = sum(students.values()) / len(students)

# Find topper
topper = max(students, key=students.get)

# Find lowest scorer
lowest = min(students, key=students.get)

print("\n-----------------------------------")
print("Total Students :", len(students))
print("Average Marks  :", round(average_marks, 2))
print("Topper          :", topper)
print("Topper Marks    :", students[topper])
print("Lowest Scorer   :", lowest)
print("Lowest Marks    :", students[lowest])
print("-----------------------------------")

print("\nProgram Executed Successfully!")
