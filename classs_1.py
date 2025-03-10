#Create a Book class with attributes title, author, and price. Add a method show_details() to display the book details.
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def show_details(self):
        return f"Title of the book is {self.title} which is written by {self.author} and it costs Rs {self.price}"
book1=Book("Godan","Ravindra nath Tagore",100)
print(book1.show_details())
