# lib/many_to_many.py

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid type for book")
        if not isinstance(date, str):
            raise Exception("Invalid type for date")
        if not isinstance(royalties, int):
            raise Exception("Invalid type for royalties")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid type for author")
        if not isinstance(book, Book):
            raise Exception("Invalid type for book")
        if not isinstance(date, str):
            raise Exception("Invalid type for date")
        if not isinstance(royalties, int):
            raise Exception("Invalid type for royalties")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Invalid type for date")
        return [contract for contract in cls.all if contract.date == date]
