#Sorting  in python .sort() or sorted()
# lists[], tuples(), Dictonaries{"":""} , Objects

# -----------list----------- #
# fruits = ["banana", "apple", "coconut","orange"]

# #fruits.sort()
# fruits.sort(reverse=True)

# print(fruits)

# ----------tuples---------#
# fruits = ("banana","apple", "coconut","orange")

# fruits = tuple(sorted(fruits, reverse = True))

# print(fruits)


# -------Dictonaries-------#
# fruits = {"banana": 105,
#           "orange": 73,
#           "apple": 72,
#           "coconut": 350
#           }

# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# print(fruits)


#-----------OBJECTS--------#
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("Banana", 105),
          Fruit("apple", 72),
          Fruit("orange", 73),
          Fruit("Coconut", 350)]

# Sort by name (ascending)
fruits_by_name = sorted(fruits, key=lambda fruit: fruit.name)
print("Sorted by name (asc):", fruits_by_name)

# Sort by name (descending)
fruits_by_name_desc = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
print("Sorted by name (desc):", fruits_by_name_desc)

# Sort by calories (ascending)
fruits_by_calories = sorted(fruits, key=lambda fruit: fruit.calories)
print("Sorted by calories (asc):", fruits_by_calories)

# Sort by calories (descending)
fruits_by_calories_desc = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)
print("Sorted by calories (desc):", fruits_by_calories_desc)
