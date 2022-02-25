"""Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным
целочисленным значением, включая 0.

Примечание: сможете ли вы замаскировать работу декоратора?"""


from functools import wraps


def check(*args, **kwargs):
    if not isinstance(args[0], int) or args[0] <= 0:
        raise ValueError(f'wrong value {args[0]}')


def val_checker(func):
    def _val_checker(ofunc):
        print('Я декоратор')
        @wraps(ofunc)
        def wrapper(*args, **kwargs):
            print('Я обертка')
            func(*args)                     #обращение к ф-и check
            res = ofunc(*args, **kwargs)    #обращение к ф-и calc_cube
            return res
        return wrapper
    return _val_checker


@val_checker(check)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))