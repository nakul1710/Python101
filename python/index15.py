# two dimentional lists

fruits = ["apple","banana","orange","coconut"]
vegetables = ["onion","Potato","carrots","ladyfinger"]
meats = ["chickens","fish","turkey","pork"]


groceries = [fruits,vegetables,meats]


print(groceries[0])
print(groceries[0][0])
print(groceries[1][3])
print(groceries)

for collection in groceries:
    print(collection)

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()


#keypad phone

num_pad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))



for row in num_pad:
    for num in row:
        print(num,end = " ")
    print()

