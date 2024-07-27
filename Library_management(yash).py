from datetime import datetime, timedelta
from datetime import date
class Library:
    def __init__(self, books):
        self.books = books

    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book["available"]:
                print(f"{book['title']} by {book['author']} ({book['publication_year']})")

    def search_book(self):
        print("\nSearch Book:")
        search_query = input("Enter title, author, or publication year: ").lower()

        for book in self.books:
            if search_query in book["title"].lower() or search_query in book["author"].lower() or search_query == book["publication_year"]:
                if book["available"]:
                    print(f"\nBook found:")
                    print(f"Title: {book['title']}")
                    print(f"Author: {book['author']}")
                    print(f"Publication Year: {book['publication_year']}")
                    print(f"Location: {book['location']}")
                else:
                    print(f"\nBook not available currently.")
                return
        print("\nBook not found.")

    def request_book(self):
        print("\nRequest Book:")
        request_query = input("Enter title of the book you want to request: ").lower()

        for book in self.books:
            if request_query == book["title"].lower():
                if book["available"]:
                    book["available"] = False
                    print("\nBook requested successfully!")
                    return
                else:
                    print("\nBook not available currently. You can reserve it if you want.")
                    return
        print("\nBook not found.")

    def reserve_book(self):
        print("\nReserve Book:")
        reserve_query = input("Enter title of the book you want to reserve: ").lower()

        for book in self.books:
            if reserve_query == book["title"].lower():
                if not book["available"]:
                    print("\nBook is already reserved. You can't reserve it again.")
                    return
                book["reserved"] = True
                print("\nBook reserved successfully!")
                return
        print("\nBook not found.")

    def renew_book(self):
        print("\nRenew Book:")
        renew_query = input("Enter title of the book you want to renew: ").lower()

        for book in self.books:
            if renew_query == book["title"].lower():
                if book["reserved"]:
                    print("\nBook is reserved. You can't renew it.")
                    return
                if book["available"]:
                    print("\nBook is not issued yet. You can't renew it.")
                    return
                book["due_date"] += timedelta(days=7)
                print("\nBook renewed successfully!")
                return
        print("\nBook not found.")

    def add_book(self):
        print("\nAdd Book:")
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        publication_year = input("Enter publication year of the book: ")
        location = input("Enter location of the book: ")
        self.books.append({"title": title, "author": author, "publication_year": publication_year, "location": location, "available": True, "reserved": False, "due_date": None})
        print("\nBook added successfully!")

    def remove_book(self):
        print("\nRemove Book:")
        remove_query = input("Enter title of the book you want to remove: ").lower()
        for book in self.books:
            if remove_query == book["title"].lower():
                self.books.remove(book)
                print("\nBook removed successfully!")
                return
        print("\nBook not Found")

    def return_book(self):
      print("\nReturn Book:")
      return_query = input("Enter title of the book you want to return: ").lower()

      for book in self.books:
        if return_query == book["title"].lower():
            if book["available"]:
                print("\nBook is not issued. You can't return it.")
                return
            book["available"] = True
            book["reserved"] = False
            book["due_date"] = None
            print("\nBook returned successfully!")
            return
      print("\nBook not Found")
print("----------------------------------LIBRARY MANAGEMENT SYSTEM--------------------------------")
books = [
{"title": "The Alchemist", "author": "Paulo Coelho", "publication_year": "1988", "location": "Fiction", "available": True, "reserved": False, "due_date": None},
  
{"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": "1960", "location": "Fiction", "available": False, "reserved": True, "due_date": date.today() + timedelta(days=7)},
  
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": "1925", "location": "Fiction", "available": False, "reserved": False, "due_date": date.today() - timedelta(days=3)},
  
{"title": "1984", "author": "George Orwell", "publication_year": "1949", "location": "Fiction", "available": True, "reserved": False, "due_date": None},
]

library =Library(books)

while True:
  print("\nMenu:")
  print("1. Display available books")
  print("2. Search book")
  print("3. Request book")
  print("4. Reserve book")
  print("5. Renew book")
  print("6. Add book")
  print("7. Remove book")
  print("8. Return book")
  print("9. Exit")
  ch1 = int(input("Enter the Choice: "))
  if ch1==1:
    library.display_available_books()
  if ch1==2:
    library.search_book()
  if ch1==3:
    library.request_book()
  if ch1==4:
    library.reserve_book()
  if ch1==5:
    library.renew_book()
  if ch1==6:
    library.add_book()
  if ch1==7:
    library.remove_book()
  if ch1==8:
    library.return_book()
  if ch1==9:
     break
