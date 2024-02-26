import doctest
from typing import Union

if __name__ == "__main__":
    class Building:
        def __init__(self, height: Union[int, float], material: str):
            """
            Создание и подготовка к работе объекта "здание"
            :param height: высота здания
            :param material: материал здания:
            >>> building1 = Building(50, "Brick")  #  инициализация экземпляра класса
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
            метод находит вес здания
            :param area: площадь этажа
            :return: вес здания в ньютонах:
            >>> building1 = Building(50, "Brick")
            >>> building1.find_weight(50)
            """

            if not isinstance(area, (int, float)):
                raise TypeError("Высота должна быть целым или числом с плавающей точкой")
            if area < 0:
                raise ValueError("Высота должна быть больше нуля")

            ...

        def find_cost(self, material: str) -> float:
            """
            метод находит стоимость здания
            :param material: материал здания
            :return: стоимость здания в млн. руб.
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
            Создание и подготовка к работе объекта "бутылка"
            :param volume:объем бутылки
            :param contents: наполнение бутылки
            :param is_empty: пустая или нет:
            >>> bottle1 = Bottle(500, "Juice", False)  # инициализация экземпляра класса
            """

            if not isinstance(volume, (int, float)):
                raise TypeError("Объем должна быть целым или числом с плавающей точкой")
            if volume < 0:
                raise ValueError("Объем должен быть больше нуля")

            if not isinstance(contents, str):
                raise TypeError("Наполнение должно быть строкой")
            if contents == "":
                raise ValueError("Наполнение не должно быть пустым")

            if not isinstance(is_empty, bool):
                raise TypeError("атрибут is_empty должен быть булевым")

            self.volume = volume
            self.contents = contents
            self.is_empty = is_empty

        def drink_bottle(self, volume: Union[int, float], is_empty: bool) -> None:
            """
            метод, отвечающий за выпивание жидкости из бутылки
            :param volume: объем бутылки
            :param is_empty: пустая или нет
            >>> bottle1 = Bottle(500, "Juice", False)
            >>> bottle1.drink_bottle(50, False)
            """

            if self.is_empty:
                raise Exception("нельзя выпить пустую бутылку")
            self.volume = volume
            self.is_empty = is_empty
            ...

        def fill_bottle(self, is_empty) -> None:
            """
            метод наполняющий бутылку
            :param is_empty: пустая или нет:
            >>> bottle1 = Bottle(500, "Juice", True)
            >>> bottle1.fill_bottle(True)
            """
            if not self.is_empty:
                raise Exception("Нельзя наполнить полную бутылку")
            self.is_empty = is_empty


    class Human:
        def __init__(self, age: int, name: str, alive: bool):
            """
            Создание и подготовка к работе объекта "Человек"
            :param age: возраст
            :param name: имя
            :param alive: жив или нет
            """
            if not isinstance(age, int):
                raise TypeError("возраст должен быть целым числом")
            if age < 0:
                raise ValueError("возраст должен быть больще нуля")

            if not isinstance(name, str):
                raise TypeError("имя должно быть строковым")
            if name == "":
                raise ValueError("имя не должно быть пустым")

            if not isinstance(alive, bool):
                raise TypeError("атрибут alive должен быть булевым")

            self.age = age
            self.name = name
            self.alive = alive

        def check_human(self, age: int, name: str, alive: bool, human_data: list) -> bool:
            """
            метод, проверяющий есть ли данный человек в базе данных human_data
            :param human_data: база данных с людьми
            :param age: возраст
            :param name: имя
            :param alive: жив или нет
            :return: присутсвует ли данный человек в базе данных
            """
            ...

        def change_param(self, age: int, name: str, alive: bool, human_data: list) -> None:
            """
            метод позволяет менять параметры в баз данных human_data
            :param human_data: база данных с людьми
            :param age: возраст
            :param name: имя
            :param alive: жив или нет
            """


    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
