"""Задание 5
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""



def get_uniq_numbers(src: list):
    uniq_nums = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            uniq_nums.add(el)
        else:
            uniq_nums.discard(el)
        tmp.add(el)
    print(uniq_nums)

    uniq_nums_ord = [el for el in src if el in uniq_nums]
    yield uniq_nums_ord



src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))