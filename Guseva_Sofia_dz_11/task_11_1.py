"""Задание 1
Реализовать класс Дата, функция-конструктор которого должна принимать дату в виде строки
формата день-месяц-год. В рамках класса реализовать два метода:

Первый — с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""

from datetime import date


class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def c_method(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f'{day}\n{month}\n{year}'
        except ValueError:
            return 'Указана неправильная дата'

    @staticmethod
    def s_method(data):
        try:
            day, month, year = data.split('-')
            return date(int(year), int(month), int(day))
        except ValueError:
            return 'Указана неправильная дата'


if __name__ == '__main__':
    print(Data.c_method('21-05-1998'))
    print(Data.c_method('21.0-13-1998'))
    print(Data.s_method('09-09-2007'))
    print(Data.s_method('21/13/1998'))
    print(Data.s_method('09-13-2007'))
