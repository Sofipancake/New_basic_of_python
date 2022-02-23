"""Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения —
общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:

{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
size = [10 ** i for i in range(2, 6)]
res_dict = dict.fromkeys(size, 0)

for root, dirs, files in os.walk(BASE_DIR):
    for name in files:
        check_size = os.path.getsize(os.path.join(root, name))
        value_dict = min(filter(lambda x: check_size < x, size))
        res_dict[value_dict] += 1

print(res_dict)



