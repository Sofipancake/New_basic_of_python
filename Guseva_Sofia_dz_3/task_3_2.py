# Задание 2 *(вместо задачи 1)
# Перепишите функцию из задания 1 изменив название на num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.

#Например:
#>>> num_translate_adv("One")
#"Один"
#>>> num_translate_adv("two")
#"два"

from string import ascii_uppercase


def num_translate_adv(value: str, str_out=None) -> str:
    """переводит числительное с английского на русский """
    num = {
        "zero": 'ноль',
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять'
    }
    if (value[0] in ascii_uppercase) and (value.lower() in num):
        return num.get(value.lower()).capitalize()
    else:
        return num.get(value)


print(num_translate_adv("one"))                #один
print(num_translate_adv("One"))                #Один
print(num_translate_adv("eight"))              #восемь
print(num_translate_adv("Five"))               #Пять
print(num_translate_adv("один"))               #None
