# Collection : Single "variable" used to stroe multiple values
#Lists = [] ordered and change-able .Duplicate ok
# Sets = {} unordered  and immutable, but add/remove ok. No Duplicates
# Tuples = () ordered and unchange-able . Duplicates are ok


##1 * Lists *


#fruits = ["Mango","banana","Coconut","Orange"]

# print(fruits[0])
# print(fruits[0::3])
# print(fruits[::-1])
# print(fruits[::2])


#print(dir(fruits))   Bunch of Functions in lists
#print(help(list))
 #print(len(fruits))

#fruits[0] = "Pinapple"
#fruits.append("Pineapple")
#fruits.remove("Mango")
#fruits.insert(0,"Pineapple")
#fruits.sort()
#fruits.reverse()
#print(fruits.index("banana"))

# for fruits in fruits:
#     print(fruits)

#print(fruits)


##2 * Sets *

#fruits = {"Mango" , "banana" , "Coconut" , "Orange"}

# fruits.add("Pineapple")
# fruits.remove("Orange")
# fruits.pop()
# fruits.clear()




#print(fruits)


##3 tuples

fruits = ("Mango" , "banana" , "Coconut" , "Orange")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pinapple" in fruits)
# print(fruits.index("Mango"))
# print(fruits.count("banana"))



print(fruits)
for fruits in fruits:
    print(fruits)


