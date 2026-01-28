# Condition expression : A one line shorcut for the if-else statements(ternary statemnts)
#                      print  or assign one of two  values based on a condition
#                       X if cond.  else y

# num = 5

# print("Positive" if num > 0 else "Negative")

# result = "Even" if num%2 == 0 else "Odd"

# print(result)


# String  Methods

#phone_number = input("Enter your phone :")

#result = len(name)
#result =  name.find("a")

#result = name.rfind("a")
# result = name.capitalize()
# result = name.upper()

# result = name.lower()
# result = name.isdigit()  only contains digits
#result = name.isalpha() only contain  chracters

# phone_number = phone_number.count("-")
# phone_number = phone_number.replace("-"," ")

# print(phone_number)



username  = input("Enter a username:")

if len(username) > 12:
        print("Username should be of 12 chracter.")
elif not username.find(" ") == -1:
        print("Username can't be contain any spaces.")
elif not username.isalpha():
        print("Your username can't contain numbers.")
else :
        print(f"welcome {username}")
        