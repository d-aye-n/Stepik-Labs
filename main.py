# -*- coding: windows-1251 -*-
import doctest
from typing import Union

if __name__ == "__main__":
    class Building:
        def __init__(self, height: Union[int, float], material: str):
            """
            �������� � ���������� � ������ ������� "������"

            :param height: ������ ������
            :param material: ������������ �������� �� �������� ������� ������

            �������:
            >>> building1 = Building(50, "Brick")  # ������������� ���������� ������
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
            ������� ������� ��� ������

            :param area: ������� ������

            :return: ��� ������ � ��
            �������:
            >>> building1 = Building(50, "Brick")
            >>> building1.find_weight(50)
            """

            if not isinstance(area, (int, float)):
                raise TypeError("������ ������ ������ ���� ���� int ��� float")
            if area < 0:
                raise ValueError("������ ������ ������ ���� ������������� ������")

            ...

        def find_cost(self, material: str) -> float:
            """
            ������� ������� ��������� ������

            :param material: ������������ �������� �� �������� ������� ������
            :return: ��������� ������

            �������:
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
            �������� � ���������� � ������ ������� "�������"

            :param volume: ����� ������� �������
            :param contents: ������ �������
            :param is_empty: ���������� ������ ������� ��� ���

            �������:
            >>> bottle1 = Bottle(500, "Juice", False)  # ������������� ���������� ������
            """

            if not isinstance(volume, (int, float)):
                raise TypeError("����� ������� ������ ���� ���� int ��� float")
            if volume < 0:
                raise ValueError("����� �������� ������ ���� ������������� ������")

            if not isinstance(contents, str):
                raise TypeError("������ ������ ���� ���� string")
            if contents == "":
                raise ValueError("������ �� ����� ���� ������")

            if not isinstance(is_empty, bool):
                raise TypeError("������� is_empty ������ ���� ���� bool")

            self.volume = volume
            self.contents = contents
            self.is_empty = is_empty

        def drink_bottle(self, volume: Union[int, float], is_empty: bool) -> None:
            """
            ������� �������� �� ����������� �������
            :param volume: ����� �������
            :param is_empty: ������ ������� ��� ���

            �������:
            >>> bottle1 = Bottle(500, "Juice", False)
            >>> bottle1.drink_bottle(50, False)
            """

            if self.is_empty:
                raise Exception("������� ��� �����")
            self.volume = volume
            self.is_empty = is_empty
            ...

        def fill_bottle(self, is_empty) -> None:
            """
            ������� ��������� �������

            :param is_empty: ������ ������� ��� ���

            �������:
            >>> bottle1 = Bottle(500, "Juice", True)
            >>> bottle1.fill_bottle(True)
            """
            if not self.is_empty:
                raise Exception("������� ������ ���� �����")
            self.is_empty = is_empty


    class Human:
        def __init__(self, age: int, name: str, alive: bool):
            """
            �������� � ���������� � ������ ������� "�������"

            :param age: �������
            :param name: ���
            :param alive: ��� �� ������ �������
            """
            if not isinstance(age, int):
                raise TypeError("������� ������ ���� ���� int ��� float")
            if age < 0:
                raise ValueError("������� ������ ���� ������������� ������")

            if not isinstance(name, str):
                raise TypeError("��� ������ ���� ���� string")
            if name == "":
                raise ValueError("��� �� ����� ���� ������")

            if not isinstance(alive, bool):
                raise TypeError("������� alive ������ ���� ���� bool")

            self.age = age
            self.name = name
            self.alive = alive

        def check_human(self, age: int, name: str, alive: bool, human_data: list) -> bool:
            """
            ������� ��������� ���� �� ������� ������� ������������� ��������� ������
            � ���� ���������

            :param human_data: ������ �������� � ������� ��������� ����������� ������
            :param age: �������
            :param name: ���
            :param alive: ��� �� ������ �������

            :return: ���� �� ������� ������� ������������� ��������� ������
            """
            ...

        def change_param(self, age: int, name: str, alive: bool, human_data: list) -> None:
            """
            ������� ��������� ������ �����-���� �������� � human_data

            :param human_data: ������ �������� � ������� ��������� ����������� ������
            :param age: �������
            :param name: ���
            :param alive: ��� �� ������ �������
            """


    if __name__ == "__main__":
        doctest.testmod()  # ������������ ��������, ������� ��������� � ������������
