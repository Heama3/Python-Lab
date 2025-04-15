# Student data will be stored as a tuple: (Name, Roll Number, (Marks1, Marks2, Marks3), Grade)

# List to store student records
students = []

# Create Students
def create_students():
    global students
    students = [
        ("Alice", 101, (85, 90, 88), "A"),
        ("Bob", 102, (78, 80, 76), "B"),
        ("Charlie", 103, (92, 89, 95), "A")
    ]

# Display All Students
def display_students():
    print("\nAll Students:")
    for s in students:
        print(f"Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}, Grade: {s[3]}")

# Add a New Student
def add_student(name, roll, marks, grade):
    students.append((name, roll, marks, grade))
    print(f"\nStudent {name} added.")
    print(students)

# Search for a Student
def search_student(roll):
    for s in students:
        if s[1] == roll:
            print(f"\nStudent Found: Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}, Grade: {s[3]}")
            return
    print("\nStudent not found.")

# Calculate Total Marks
def calculate_total_marks():
    print("\nTotal Marks for Each Student:")
    for s in students:
        total = sum(s[2])
        print(f"Roll No: {s[1]}, Name: {s[0]}, Total Marks: {total}")

# Update Grades
def update_grade(roll, new_grade):
    for i, s in enumerate(students):
        if s[1] == roll:
            students[i] = (s[0], s[1], s[2], new_grade)
            print(f"\nGrade updated for Roll No: {roll}")
            return
    print("\nStudent not found.")

# Remove a Student
def remove_student(roll):
    global students
    students = [s for s in students if s[1] != roll]
    print(f"\nStudent with Roll No: {roll} removed if existed.")

# Example Usage
create_students()
display_students()
add_student("Diana", 104, (88, 91, 85), "A")
search_student(102)
calculate_total_marks()
update_grade(103, "A+")
remove_student(101)
display_students()
