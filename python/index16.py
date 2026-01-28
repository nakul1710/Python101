#dictionary = a collection of {key:value} pairs
#            ordered and changeable. No duplicates

Capitals = { "Usa": "Wasington Dc",
             "India": "New Delhi",
             "Russia": "Moscow",
             "China": "Bejing"
            }

# print(dir(Capitals))
# print(help(Capitals))
# print(Capitals.get("India"))
# print(Capitals.get("Japan"))  # None

# if Capitals.get("India"):
#     print("That Capital exists")
# else:
#     print("This capital doesn't exist")


# Capitals.update({"Germany": "Berlin"})
# Capitals.update({"India": "Jaipur"})
# Capitals.pop("China")
# Capitals.popitem()
# Capitals.clear()

# print(Capitals)

# Keys = Capitals.keys()
# print(Keys)

# values = Capitals.values()
# print(values)

# for values in Capitals.values:
#     print(values)

items = Capitals.items()
print(items)
for key,value in Capitals.items():
    print(f"{key}:{value}")





