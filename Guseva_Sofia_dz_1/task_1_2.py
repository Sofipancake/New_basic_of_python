# Задача-2: a) Создать список, состоящий из кубов нечётных
# чисел от 1 до 1000 (куб X - третья степень числа X):
# # Вычислить сумму тех чисел из этого списка, сумма цифр
# которых делится нацело на 7.
# b) К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7.
# *c) Решить задачу под пунктом b, не создавая новый список.
# (если будете решать - либо создайте доп. функцию, либо
# перепишите существующую sum_list_2)

# """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""

def sum_list_1(dataset: list) -> int:
    res = 0
    for i in range(len(dataset)):
        a = dataset[i]
        s = 0
        while a > 0:
            s = s + a % 10
            a = a // 10
        if s % 7 == 0:
            res = res + dataset[i]
    return res

#   """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
 #     сумма цифр которых делится нацело на 7"""

def sum_list_2(dataset: list) -> int:
    res = 0
    for i in range(len(dataset)):
        a = dataset[i] + 17
        s = 0
        while a > 0:
            s = s + a % 10
            a = a // 10
        if s % 7 == 0:
            res = res + dataset[i]
    return res

my_list = [i for i in range(1,1000,2)]# Соберите нужный список по заданию
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 3
print(my_list)

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)