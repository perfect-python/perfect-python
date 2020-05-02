from typing import TypedDict


class Book(TypedDict):
    name: str
    author: str
    price: int


if __name__ == '__main__':
    book1:Book = {'name': 'Spam', 'author': 'soseki', 'price': 300}
    book2:Book = {}
    book3:Book = {'name': 'Spam', 'writer': 'ogai', 'price': 450}

