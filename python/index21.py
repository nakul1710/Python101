#Function = A block of refusable code
#           place() after the function  name to invoke it


# def happy_birthday(name,age):
#      print(f"Happy Birthday to {name}!")
#      print(f"You are {age} years old")
#      print("Happy Birthday to you!")


# happy_birthday("Bro",20)
# happy_birthday("Steve",30)
# happy_birthday("Harrinton",25)


# return = statement used to end a function.
#         and send a result back to the caller.



# def add(x,y):
#     z = x+y
#     return z

# def sub(x,y):
#     z = x-y
#     return z

# def mul(x,y):
#     z = x*y
#     return z

# def div(x,y):
#     z = x/y
#     return z


# print(add(3,5))
# print(sub(3,5))
# print(mul(3,5))
# print(div(3,5))



def full_name(first, last):
    """
    Returns the full name with each part capitalized.
    """
    return f"{first.capitalize()} {last.capitalize()}"

print(full_name("nakul", "yadav"))
