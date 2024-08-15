import mysql.connector
from datetime import datetime, timedelta

class Library:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def display_available_books(self):
        self.cursor.execute("SELECT * FROM books WHERE available = TRUE")
        books = self.cursor.fetchall()
        print("\nAvailable Books:")
        for book in books:
            print(f"{book['title']} by {book['author']} ({book['publication_year']})")

    def search_book(self):
        print("\nSearch Book:")
        search_query = input("Enter title, author, or publication year: ").lower()
        self.cursor.execute("""
            SELECT * FROM books 
            WHERE LOWER(title) LIKE %s OR LOWER(author) LIKE %s OR publication_year = %s
        """, (f'%{search_query}%', f'%{search_query}%', search_query))
        book = self.cursor.fetchone()
        if book:
            if book["available"]:
                print(f"\nBook found:")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Publication Year: {book['publication_year']}")
                print(f"Location: {book['location']}")
            else:
                print(f"\nBook not available currently.")
        else:
            print("\nBook not found.")

    def request_book(self):
        print("\nRequest Book:")
        request_query = input("Enter title of the book you want to request: ").lower()
        self.cursor.execute("SELECT * FROM books WHERE LOWER(title) = %s", (request_query,))
        book = self.cursor.fetchone()
        if book:
            if book["available"]:
                self.cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book['id'],))
                self.conn.commit()
                print("\nBook requested successfully!")
            else:
                print("\nBook not available currently. You can reserve it if you want.")
        else:
            print("\nBook not found.")

    def reserve_book(self):
        print("\nReserve Book:")
        reserve_query = input("Enter title of the book you want to reserve: ").lower()
        self.cursor.execute("SELECT * FROM books WHERE LOWER(title) = %s", (reserve_query,))
        book = self.cursor.fetchone()
        if book:
            if book["reserved"]:
                print("\nBook is already reserved. You can't reserve it again.")
            else:
                self.cursor.execute("UPDATE books SET reserved = TRUE WHERE id = %s", (book['id'],))
                self.conn.commit()
                print("\nBook reserved successfully!")
        else:
            print("\nBook not found.")

    def renew_book(self):
        print("\nRenew Book:")
        renew_query = input("Enter title of the book you want to renew: ").lower()
        self.cursor.execute("SELECT * FROM books WHERE LOWER(title) = %s", (renew_query,))
        book = self.cursor.fetchone()
        if book:
            if book["reserved"]:
                print("\nBook is reserved. You can't renew it.")
            elif book["available"]:
                print("\nBook is not issued yet. You can't renew it.")
            else:
                new_due_date = datetime.now() + timedelta(days=7)
                self.cursor.execute("UPDATE books SET due_date = %s WHERE id = %s", (new_due_date, book['id']))
                self.conn.commit()
                print("\nBook renewed successfully!")
        else:
            print("\nBook not found.")

    def add_book(self):
        print("\nAdd Book:")
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        publication_year = input("Enter publication year of the book: ")
        location = input("Enter location of the book: ")
        self.cursor.execute("""
            INSERT INTO books (title, author, publication_year, location)
            VALUES (%s, %s, %s, %s)
        """, (title, author, publication_year, location))
        self.conn.commit()
        print("\nBook added successfully!")

    def remove_book(self):
        print("\nRemove Book:")
        remove_query = input("Enter title of the book you want to remove: ").lower()
        self.cursor.execute("SELECT * FROM books WHERE LOWER(title) = %s", (remove_query,))
        book = self.cursor.fetchone()
        if book:
            self.cursor.execute("DELETE FROM books WHERE id = %s", (book['id'],))
            self.conn.commit()
            print("\nBook removed successfully!")
        else:
            print("\nBook not found.")

    def return_book(self):
        print("\nReturn Book:")
        return_query = input("Enter title of the book you want to return: ").lower()
        self.cursor.execute("SELECT * FROM books WHERE LOWER(title) = %s", (return_query,))
        book = self.cursor.fetchone()
        if book:
            if book["available"]:
                print("\nBook is not issued. You can't return it.")
            else:
                self.cursor.execute("""
                    UPDATE books
                    SET available = TRUE, reserved = FALSE, due_date = NULL
                    WHERE id = %s
                """, (book['id'],))
                self.conn.commit()
                print("\nBook returned successfully!")
        else:
            print("\nBook not found.")

# Initialize the Library with MySQL connection parameters
library = Library(host="localhost", user="root", password="###########", database="library_db")

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
    if ch1 == 1:
        library.display_available_books()
    elif ch1 == 2:
        library.search_book()
    elif ch1 == 3:
        library.request_book()
    elif ch1 == 4:
        library.reserve_book()
    elif ch1 == 5:
        library.renew_book()
    elif ch1 == 6:
        library.add_book()
    elif ch1 == 7:
        library.remove_book()
    elif ch1 == 8:
        library.return_book()
    elif ch1 == 9:
        break
