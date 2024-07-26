# Please write a function named books_of_genre(books: list, genre: str) which takes a list of objects of type Book and a string representing a genre as its arguments.

# The function should return a new list, which contains the books with the desired genre from the original list.



# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# Write your solution here
# -----------------------------

def books_of_genre(books: list, genre: str):
    new_list = []
    for book in books:
        if book.genre == genre:
            new_list.append(book)

    return new_list