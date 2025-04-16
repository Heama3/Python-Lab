#key -value in dictionary

student_marks={
    "Heama":89,
    "Keerthy":90,
    "Kavya":95
    }
name=input("Enter the student name:")
if name in student_marks:
    print(f"{name} marks:{student_marks[name]}")
else:
    print("Student not found")

