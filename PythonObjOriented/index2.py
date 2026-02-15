class Student:

    class_year = 2024
    num_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("Spongbob",30)
student2 = Student("Patrick",27)
student3 = Student("Yuvraj",22)
student4 = Student("Nakul",20)


print(student2.name)
print(student2.age)

print(student1.name)
print(student1.age)

print(student3.name)
print(student3.age)

print(student4.name)
print(student4.age)





print(f"My graduating class of {Student.class_year} has {Student.num_student} students")