class Student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.marks)

# List to store students
students = []

# Take input for number of students
n = int(input("Enter the number of students: "))

# Take input for each student
for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    usn = input("USN: ")
    name = input("Name: ")
    marks = int(input("Marks: "))
    student = Student(usn, name, marks)
    students.append(student)

# Find the highest marks
highest_marks = max(student.marks for student in students)

# Display students with the highest marks
print("\nStudent(s) with the highest marks:")
for student in students:
    if student.marks == highest_marks:
        student.display()
        print()
