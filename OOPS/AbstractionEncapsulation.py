#Example to implement Abstraction and Encapsulation in Python
'''Library management system
    ->Customer should be able to display all the books available in Library
    ->Handle the process when a customer requests to borrow a book
    ->Update the library collection when the customer returns a book'''
class Library:
    def __init__(self,bookList):
        self.bookList = bookList

    def displayAvailableBooks(self):
        print("\n Available Books: ")
        for book in self.bookList:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.bookList:
            print("You have borrowed ",requestedBook," book.")
            self.bookList.remove(requestedBook)
            return requestedBook
        else:
            print("Sorry Book is not Available.")
            return "No Book"

    def addBook(self,returnBook):
        if returnBook != "No Book":
            self.bookList.append(returnBook)
            print("You have added ",returnBook," book to Library, Thank You.")

class Customer:
    def __init__(self):
        self.book="No Book"

    def requestBook(self):
        self.book = input("Enter The book you want from Library: ")
        return self.book

    def returnBook(self):
        myBook = "No Book"
        if self.book != "No Book":
            print("Returning ",self.book)
            myBook = self.book
            self.book ="No Book"
        else:
            print("Carrying No Book")
        return myBook

library = Library(['Book1','Book2','Book3','Book4'])
customer = Customer()
usrChoice=0
while usrChoice < 5:
    print("\n1. Display the Available Books \n2. Borrow a Book \n3. Return a Book \n4. Donate a Book \n5. Exit from Library\n ")
    usrChoice=int(input("Enter your Choice: "))
    if usrChoice == 1:
        library.displayAvailableBooks()
    elif usrChoice == 2:
        book = library.lendBook(customer.requestBook())
        if  book != "No Book":
            customer.book = book
    elif usrChoice == 3:
        library.addBook(customer.returnBook())
    elif usrChoice == 4:
        donateBook = input("Enter The book you want to donate to Library: ")
        library.addBook(donateBook)
        library.displayAvailableBooks()
    else:
        break
