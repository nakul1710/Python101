#List Comprehension = A concise way to create lists in python 
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
# print(doubles) 


doubles = [x * 2 for x in range(1,11)]
triples = [x * 3 for x in range(1,11)]
squares = [x * x for x in range(1,11)]

print(doubles)
print(triples)
print(squares)




#Strings

fruits = ["apple","orange","banana","cocunut"]
fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit[0] for fruit in fruits]

print(fruits)



numbers = [1,-2, 3, -4, 5 , -6]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for  num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

