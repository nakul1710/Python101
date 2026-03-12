#Genrator = Function that behave like an iterators (it can be used in a for loop)

def cout_no(n):
    numbers = []
    count = 1
    while count <= n:
        numbers.append(count)
        count += 1
    return numbers


numbers = int(input("Enter a number:"))

for n in cout_no(numbers):
    print(n)

