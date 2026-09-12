class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


s1 = Student("Rahul", 101, 85.5)

print("Student Name:", s1.name)
print("Roll Number:", s1.roll)
print("Marks:", s1.marks)