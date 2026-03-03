#lambda function = A small anonymous function for one time use(throw away function)
#                  take any number of aguemnts , but have only one 1 expression
#                  Helps keep the namespace clean is useful with higher order function
#                  'Sort()' , 'map()' , 'filter()' , 'reduce()'

double = lambda x : x * 2
add = lambda x,y : x+y
max_value = lambda x, y : x if x>y else y
min_value = lambda x, y : x if x<y else y
fullname = lambda  first, last: first + " " + last
is_even = lambda x : x%2 == 0

# print(double(4))
# print(add(3,9)) 
# print(max_value(8,9))
# print(min_value(7,3))
# print("Nakul","Yadav")
#print(is_even(4))



