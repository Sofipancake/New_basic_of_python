"""Задание 2
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class MyException(Exception):
    """Исключение, обрабатывающее деление на 0"""
    def __init__(self, txt):
        self.txt = txt

f_dig = input('Введите делимое ')
s_dig = input('Введите делитель ')

try:
    f_dig = int(f_dig)
    s_dig = int(s_dig)
    if s_dig == 0:
        raise MyException('На ноль делить нельзя')
except ValueError:
    print('Введено не число')
except MyException as err:
    print(err)
else:
    res = f_dig / s_dig
    print(f'Результат деления {f_dig} на {s_dig} = {res}')
