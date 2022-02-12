"""Задание 5
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""


#Попытка решить по-другому
def get_uniq_numbers(src: list):
    for el in src:
        if src.count(el) == 1:
            yield el


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))

#Решение как на уроке

"""
def get_uniq_numbers(src: list):
    uniq_nums = set()
    tmp = set()
    for num in src:
        if num not in tmp:
            uniq_nums.add(num)
        else:
            uniq_nums.discard(num)
        tmp.add(num)
    return [num for num in src if num in uniq_nums]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
"""
