# -*- coding: windows-1251 -*-

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO �������� ����� Book
class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'����� "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


# TODO �������� ����� Library
class Library:
    def __init__(self, books = []):
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
        raise ValueError("����� � ������������� id �� ����������")



if __name__ == '__main__':
    empty_library = Library()  # �������������� ������ ����������
    print(empty_library.get_next_book_id())  # ��������� ��������� id ��� ������ ����������

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # �������������� ���������� � �������
    print(library_with_books.get_next_book_id())  # ��������� ��������� id ��� �������� ����������

    print(library_with_books.get_index_by_book_id(1))  # ��������� ������ ����� � id = 1