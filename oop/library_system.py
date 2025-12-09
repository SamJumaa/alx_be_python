class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title } by {self.author}"
    
#creating Ebook child class
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)   ## Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
        
#creating Printbook child class

class PrintBook(Book):
    def __init__(self, title, author, page_count :int):
        super().__init__(title, author)  # # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, page count: {self.page_count}"
    
# Composition Class: Library
class Library:
    def __init__(self):
        self.books = []   # List to store books (composition)

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

  
       

    

#usage
