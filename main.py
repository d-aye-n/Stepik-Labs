# -*- coding: windows-1251 -*-

class Book:
    """ Áàçîâûé êëàññ êíèãè. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Êíèãà {self.name}. Àâòîð {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Êîëè÷åñòâî ñòðàíèö äîëæíî áûòü ïîëîæèòåëüíûì öåëûì ÷èñëîì.")
        self.pages = value

    # Ìåòîäû íóæíî ïåðåãðóçèòü òàê êàê â áàçîâîì êëàññå îñòóòñòâóåò àòðèáóò pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Äëèòåëüíîñòü äîëæíà áûòü ïîëîæèòåëüíûì ÷èñëîì.")
        self.duration = value

    # Ìåòîäû íóæíî ïåðåãðóçèòü òàê êàê â áàçîâîì êëàññå îñòóòñòâóåò àòðèáóò duration
    def __str__(self):
        return f"Êíèãà {self.name}. Àâòîð {self.author}. Äëèòåëüíîñòü: {self.duration} ÷àñîâ"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
