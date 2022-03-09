"""Реализовать проект Операции с комплексными числами.

Создать класс Комплексное число.
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и
умножение созданных экземпляров.
Проверить корректность полученного результата."""


class Complexdigit:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        add_re = self.re + other.re
        add_im = self.im + other.im
        return f'Сумма комплексных чисел равна: {add_re}+{add_im}*i'

    def __mul__(self, other):
        mul_re = self.re * other.re - self.im * other.im
        mul_im = self.re * other.im + other.re * self.im
        return f'Произведение комплексных чисел равно: {mul_re}+{mul_im}*i'


if __name__ == '__main__':
    a = Complexdigit(-6, 10)
    b = Complexdigit(4, 3)
    print(a + b)        #Сумма комплексных чисел равна: -2+13*i
    print(a * b)        #Произведение комплексных чисел равно: -54+22*i
    a = Complexdigit(5, -9)
    b = Complexdigit(-22, 0)
    print(a + b)        #Сумма комплексных чисел равна: -17+-9*i
    print(a * b)        #Произведение комплексных чисел равно: -110+198*i
