# Generator = Function that behaves like an iterator (it can be used in a for loop)

def count_no(n):
    count = 1
    while count <= n:
        yield count
        count += 1

numbers = int(input("Enter a number: "))

for n in count_no(numbers):
    print(n)

# For characters

def char_generator(text):
    for ch in text:
        yield ch

word = input("Enter a word: ")

for c in char_generator(word):
    print(c)