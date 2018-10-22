# Library Management System
# Library - Lend book - Available Books - Add a Book
# Customer - Request and Return Book

class Library:
    def __init__(self,listOfBooks):
        self.availableBooks=listOfBooks

    def displayAvailableBooks(self):
        print()
        for book in self.availableBooks:
            print (book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list")

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("Your book has been returned")


class Customer():
    def requestBook(self):
        print("Enter the name of the book you would like to borrow:")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of book you wish to return: ")
        self.book=input()
        return self.book

library=Library(["Think and grow rich","Who will cry when you die","One more day"])
customer=Customer()
while True:
    print("Enter 1 to display the available Books")
    print("Enter 2 to request a Book")
    print("Enter 3 to return a Book")
    print("Enter 4 to exit")
    userChoice=int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook=customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnBook=customer.returnBook()
        library.addBook(returnBook)
    elif userChoice is 4:
        quit()


