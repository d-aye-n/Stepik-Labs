# -*- coding: windows-1251 -*-

class Book:
    """ ������� ����� �����. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"����� {self.name}. ����� {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("���������� ������� ������ ���� ������������� ����� ������.")
        self.pages = value

    # ������ ����� ����������� ��� ��� � ������� ������ ����������� ������� pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("������������ ������ ���� ������������� ������.")
        self.duration = value

    # ������ ����� ����������� ��� ��� � ������� ������ ����������� ������� duration
    def __str__(self):
        return f"����� {self.name}. ����� {self.author}. ������������: {self.duration} �����"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book = Book("pupa", "lupa")
    p_book = PaperBook("pupa", "lupa", 3)
    a_book = AudioBook("pupa", "lupa", 15.3)
    print(a_book.__repr__())
    print(p_book.__str__())
