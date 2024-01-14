# -*- coding: windows-1251 -*-
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if (not isinstance(capacity_volume, (int, float)) or
                isinstance(occupied_volume, (int, float))):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError
        if capacity_volume < occupied_volume:
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass

    glass2 = Glass(800, 400)
    # TODO попробовать инициализировать не корректные объекты
    glass3 = Glass(100, 200)
    glass4 = Glass(-100, 50)
