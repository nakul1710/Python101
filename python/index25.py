#Membership operator = used to test whether value or variables found in sequence 
#                      (string,list,tuple,set, or dictionry)
#                       1. in
#                       2. not in

#String
# Word = "Apple"

# letter = input("Guess a letter in a secret word:")


# if letter not in Word:
#     print(f"{letter} is not found")
# else:
#     print(f"There is a {letter}")



# students = {"spoongbon","Patrik","Sandy"}

# student = input("Enter the student name:")


# if student not in students:
#     print(f"{student} not found")
# else:
#     print(f"{student} found")


#Dictionry

# grades = {"Sandy" : "A",
#           "Squidward": "B",
#           "Patrik" : "C",
#           "Spongbob": "D"
#           }

# student = input("Enter the name of the student:")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else :
#     print(f"{student} was not found")


email = "nakulyadav1710@gmail.com"


if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")