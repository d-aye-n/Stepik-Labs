# -*- coding: windows-1251 -*-
import doctest
from typing import Union

if __name__ == "__main__":
    class Building:
        def __init__(self, height: Union[int, float], material: str):
            """
            Создание и подготовка к работе объекта "Здание"

            :param height: высота здания
            :param material: строительный материал из которого сделано здание

            Примеры:
            >>> building1 = Building(50, "Brick")  # инициализация экземпляра класса
            """
            if not isinstance(height, (int, float)):
                raise TypeError
            if height < 0:
                raise ValueError
            if not isinstance(material, str):
                raise TypeError
            if material == "":
                raise ValueError

            self.height = height
            self.material = material

        def find_weight(self, area: Union[int, float]) -> float:
            """
            Функция находит вес здания

            :param area: Площадь здания

            :return: вес здания в кН
            Примеры:
            >>> building1 = Building(50, "Brick")
            >>> building1.find_weight(50)
            """

            if not isinstance(area, (int, float)):
                raise TypeError("Высота здания должна быть типа int или float")
            if area < 0:
                raise ValueError("Высота здания должна быть положительным числом")

            ...

        def find_cost(self, material: str) -> float:
            """
            Функция находит стоимость здания

            :param material: строительный материал из которого сделано здание
            :return: стоимость здания

            Примеры:
            >>> building1 = Building(50, "Brick")
            >>> building1.find_cost("Brick")
            """
            if not isinstance(material, str):
                raise TypeError
            if material == "":
                raise ValueError
            self.material = material
            ...


    class Bottle:
        def __init__(self, volume: Union[int, float], contents: str, is_empty: bool):
            """
            Создание и подготовка к работе объекта "Бутылка"

            :param volume: Объем бутылки напитка
            :param contents: Состав напитка
            :param is_empty: Показывает пустая бутылка или нет

            Примеры:
            >>> bottle1 = Bottle(500, "Juice", False)  # инициализация экземпляра класса
            """

            if not isinstance(volume, (int, float)):
                raise TypeError("Объем бутылки должен быть типа int или float")
            if volume < 0:
                raise ValueError("Объем сбутылки должен быть положительным числом")

            if not isinstance(contents, str):
                raise TypeError("Состав должен быть типа string")
            if contents == "":
                raise ValueError("Состав не может быть пустым")

            if not isinstance(is_empty, bool):
                raise TypeError("Атрибут is_empty должен быть типа bool")

            self.volume = volume
            self.contents = contents
            self.is_empty = is_empty

        def drink_bottle(self, volume: Union[int, float], is_empty: bool) -> None:
            """
            Функция отвечает за опустошение бутылки
            :param volume: объем бутылки
            :param is_empty: пустая бутылка или нет

            Примеры:
            >>> bottle1 = Bottle(500, "Juice", False)
            >>> bottle1.drink_bottle(50, False)
            """

            if self.is_empty:
                raise Exception("Бутылка уже пуста")
            self.volume = volume
            self.is_empty = is_empty
            ...

        def fill_bottle(self, is_empty) -> None:
            """
            Функция заполняет бутылку

            :param is_empty: пустая бутылка или нет

            Примеры:
            >>> bottle1 = Bottle(500, "Juice", True)
            >>> bottle1.fill_bottle(True)
            """
            if not self.is_empty:
                raise Exception("Бутылка должна быть пуста")
            self.is_empty = is_empty


    class Human:
        def __init__(self, age: int, name: str, alive: bool):
            """
            Создание и подготовка к работе объекта "Человек"

            :param age: Возраст
            :param name: Имя
            :param alive: Жив ли данный человек
            """
            if not isinstance(age, int):
                raise TypeError("Возраст должен быть типа int или float")
            if age < 0:
                raise ValueError("Возраст должен быть положительным числом")

            if not isinstance(name, str):
                raise TypeError("Имя должно быть типа string")
            if name == "":
                raise ValueError("Имя не может быть пустым")

            if not isinstance(alive, bool):
                raise TypeError("Атрибут alive должен быть типа bool")

            self.age = age
            self.name = name
            self.alive = alive

        def check_human(self, age: int, name: str, alive: bool, human_data: list) -> bool:
            """
            Функция проверяет есть ли человек который соответствует введенным данным
            в базе программы

            :param human_data: Список словарей в которых находятся проверяемые данные
            :param age: Возраст
            :param name: Имя
            :param alive: Жив ли данный человек

            :return: Есть ли человек который соответствует введенным данным
            """
            ...

        def change_param(self, age: int, name: str, alive: bool, human_data: list) -> None:
            """
            Функция позволяет менять какой-либо параметр в human_data

            :param human_data: Список словарей в которых находятся проверяемые данные
            :param age: Возраст
            :param name: Имя
            :param alive: Жив ли данный человек
            """


    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
