class Student():
    def __init__(self,student_name,marks):
        self.student_name = student_name
        self.marks = marks
student1 = Student('Mark',88)
student2 = Student('Mary',90)
student3 = Student('Luke',86)
print(student2.student_name)
student2.student_name='Joan'
print(student2.student_name)
print(student1.student_name)
print(student3.student_name)
print(student1.marks)
print(f'{student1.student_name} your marks are {student1.marks}')
student1.marks = 97
print(f'{student1.student_name} your marks are {student1.marks}')
