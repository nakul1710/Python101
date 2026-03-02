#Class Method = Allows operations related to the class itself 
#               Takes class as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0  # Fixed: added total_gpa as class attribute

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa 

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f}"

student1 = Student("Nakul", 3.1)
student2 = Student("Patrik", 3.4)
student3 = Student("Janit", 3.6)

print(Student.get_count())
print(f"Average GPA: {Student.get_average_gpa()}")