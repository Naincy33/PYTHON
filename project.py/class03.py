class student:
    def __init__(self, usn, name ,marks):
        self.name= name
        self.usn= usn
        self.marks= marks

    def display(self):
        print("Name:" , self.name)
        print("USN:", self.usn)
        print("Marks:", self.marks)

student1=student("Naincy", "1BF24CS186", 99)
student2=student("Mimansa", "1BF24CS173", 33)

print("Student with highest marks")

if student1.marks>student2.marks:
    student1.display()

elif student2.marks>student1.marks:
    student2.display()

else:
    print("Both are equal")