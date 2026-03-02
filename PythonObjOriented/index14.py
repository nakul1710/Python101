# Magic method = Dunder method (double underscore) __init__, __str__, __eq__ are automatically called by many of 
# Python built-in operations

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self,other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return self.num_pages + other.num_pages

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit", "J.R.R. Rowling", 300)
book2 = Book("The Harry Potter", "J.R.R. Toinstik", 350)
book3 = Book("The Whale", "J.R.R. Rutherford", 400)

print(book1)

print(book1 == book2)

print(book1 < book2)

print(book3 > book2)

print(book1 + book2)

print("Whale" in book3)

print(book3['title'])

