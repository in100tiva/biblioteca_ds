
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_rented = False
        self.rent_date = None
        self.return_date = None

    def __str__(self):
        status = "Disponível" if not self.is_rented else f"Alugado até {self.return_date.strftime('%d/%m/%Y')}"
        return f"{self.title} por {self.author} ({status})"

class User:
    def __init__(self, name):
        self.name = name
        self.rented_books = []

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def list_users(self):
        for user in self.users:
            print(user)

    def rent_book(self, user, book):
        if book in self.books and not book.is_rented:
            book.is_rented = True
            book.rent_date = datetime.now()
            book.return_date = book.rent_date + timedelta(days=7)
            user.rented_books.append(book)
            print(f"{user.name} alugou {book.title}. Previsão de entrega: {book.return_date.strftime('%d/%m/%Y')}")
        else:
            print(f"{book.title} não está disponível para aluguel.")

    def return_book(self, user, book):
        if book in user.rented_books:
            book.is_rented = False
            book.rent_date = None
            book.return_date = None
            user.rented_books.remove(book)
            print(f"{user.name} devolveu {book.title}.")
        else:
            print(f"{user.name} não possui {book.title} alugado.")
