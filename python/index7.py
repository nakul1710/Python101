# String Indexing: = accessing elements of sequence using [] (indexing operator)
#   [start : end : step]


credit_number = "7582-7781-8282-6732"

#print(credit_number[3])
#print(credit_number[0:4])
#print(credit_number[5:9])
# print(credit_number[5:]) #rest of the chracter after index 5
# print(credit_number[-1]) #print all digit in reverse of the string
# print(credit_number[::2])
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


reverse_digit_number = credit_number[::-1]
print(f"{reverse_digit_number}")


email = input("Enter your Email:")

index = email.index('@')

username = email[:index]
domain = email[index+1:]

print(f"Your username is {username} and domain is {domain}")