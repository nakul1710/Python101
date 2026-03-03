#Zip() = Combine multiple iterables (lists, tuples, sets, dict)
#        into a single iterator
#        makes managing multiple indices easier

names = ["Spoongbob", "patrick", "squidward"] 
ages = [30,40,25]
jobs = ["cook","SoftwareEngineer","Cashier"]

# data = set(zip(names,ages))
# data = list(zip(names,ages))
# data = dict(zip(names,ages))

data = zip(names, ages, jobs)

for name, age, job in data:
    print(f"{name} is a {age} year old {job}")

print(data)