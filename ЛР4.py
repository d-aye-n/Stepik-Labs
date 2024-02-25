from math import sin, pi


class Quadrilateral:
    """Базовый класс для геометрических четырехугольников."""

    def __init__(self, name: str, a: float, b: float, angle: float):
        """
        Конструктор класса Quadrilateral.

        Args(Непубличные так как параметры фигуры не
        должны быть доступны для изменения после ее однозначного опредления):
            name (str): Имя четырехугольника.
            a (float): Длина стороны a.
            b (float): Длина стороны b.
            angle (float): Угол между сторонами.
        """
        self._name = name
        self._a = a
        self._b = b
        self._angle = angle

    def area(self) -> float:
        """Метод для вычисления площади фигуры."""
        return self._a * self._b * sin(self._angle)

    def perimeter(self) -> float:
        """Метод для вычисления периметра фигуры."""
        return (self._a + self._b) * 2

    def __str__(self) -> str:
        return f"Четырехугольник {self._name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name})"


class Rectangle(Quadrilateral):
    """Класс для прямоугольника."""

    def __init__(self, name: str, a: float, b: float, angle: float = pi / 2):
        """
        Конструктор класса Rectangle.

        Args:
            name (str): Имя прямоугольника.
            a (float): Длина стороны a.
            b (float): Длина стороны b.
            angle (float, optional): Угол между сторонами. По умолчанию pi/2.
        """
        super().__init__(name, a, b, angle)
        self._angle = None

    # Метод определения площади необходимо перегрузить
    # Метод определения периметра наследуется из базового класса
    def area(self) -> float:
        """Метод для вычисления площади прямоугольника."""
        return self._a * self._b

    # Магические методы необходимо перегрузить (добавились парметры)
    def __str__(self) -> str:
        return f"Прямоугольник: {self._name}, длина={self._a}, ширина={self._b}"

    def __repr__(self) -> str:
        return f"Rectangle(name={self._name}, length={self._a}, width={self._b})"


class Parallelogram(Quadrilateral):
    """Класс для параллелограмма."""

    def __init__(self, name: str, a: float, b: float, angle: float):
        """
        Конструктор класса Parallelogram.

        Args:
            name (str): Имя параллелограмма.
            a (float): Длина стороны a.
            b (float): Длина стороны b.
            angle (float): Угол между сторонами.
        """
        super().__init__(name, a, b, angle)

    # Методы определения площади и периметра наследуются из базового класса

    # Магические методы необходимо перегрузить (добавились парметры)
    def __str__(self) -> str:
        return f"Параллелограм: {self._name}, длина={self._a}, ширина={self._b}, угол={self._angle}"

    def __repr__(self) -> str:
        return f"Parallelogram(name={self._name}, length={self._a}, width={self._b}, angle={self._angle})"


if __name__ == "__main__":
    par = Parallelogram('ABCD', 10, 20, pi / 6)
    rect = Rectangle('ABCD', 10, 20)
    print(par)
    print(par.area(), par.perimeter())
    print(rect)
    print(rect.area(), rect.perimeter())
