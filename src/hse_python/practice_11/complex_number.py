# title Complex number
# description
# Реализовать класс для комплексных чисел ComplexNumber. Основные операции: сложение, вычитание, умножение, модуль числа.
# Покрыть тестами.
# end
import math


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return ComplexNumber(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __format__(self, format_spec: str) -> str:
        return self.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"{self.x} + {self.y}i"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
