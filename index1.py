# Typecasting : the process of converting a variable from one Datatype to another
# str(),int(),float(), bool()

age = 20
name = "Nakul"
gpa = 8.0
is_student = True

#type
print(type(is_student))
print(type(name))

#typecasting
gpa = int(gpa)
gpa += 1
print(gpa)

age = float(age)
print(age)

is_student = str(is_student)
print(is_student)

age = str(age)
age += "1"
print(age)

name = bool(name)
print(name) //True
# if name = ""  // False









