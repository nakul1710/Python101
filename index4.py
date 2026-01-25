#if statements

# age = int(input("Enter your age:"))

# if age >= 100:
#         print("Too old to sign up")
# elif age >=18:
#         print("You can sign up")
# elif age < 0:
#         print("You are not born yet")
# else:
#         print("You must be 18+ to sign up")


#python calculator

# operator = input("Enter the operator(+,-,*,/):")
# num1 = float(input("Enter num1:"))
# num2 = float(input("Enter num2:"))

# if operator == "+":
#     result = num1+num2
#     print(round(result,2))
# elif operator == "-":
#     result = num1-num2
#     print(round(result,2))
# elif operator == "*":
#     result = num1*num2
#     print(round(result,2))
# elif operator == "/":
#     result = num1/num2
#     print(round(result,2))
# else:
#     print(f"{operator} is not valid")



# weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilogram or pounds? (k or L):")


if unit == "K":
        weight = round(weight * 2.205,2)
        unit = "Lbs"
elif unit == "L":
        weight = round(weight / 2.205,2)
        unit = "Kgs"
else :
     print(f"{unit} is not valid")



print(f"Your weight is: {weight}{unit}")

