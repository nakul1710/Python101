#While loop


#ex1
# name = input("Enter your name:")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name:")

# print(f"Hello {name}")

#ex2

# age = int(input("Enter youe age:"))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age:"))

# print(f"You are {age} years old")

#ex3

# food = input("Enter a food you like or q to quit:")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("enter your food or q to quit:")


# print("Thank for your time ,bye!")


#ex4
num = int(input("Enter a number between 1 and 10:"))


while num<1 or num>10:
    print("Number must be between 1 and 10")
    num = int(input("Enter a number between 1 and 10:"))

print(f"You have entered {num}")
