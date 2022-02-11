#Задание 3
#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

#Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
#{
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
#}

#Подумайте:
#полезен ли будет вам оператор распаковки?
#Как поступить, если потребуется сортировка по ключам?
#Можно ли использовать словарь в этом случае?


def thesaurus(*args) -> dict:
    """" формирует словарь, в котором ключи - первые буквы имен, а значения - имена начинающиеся с соответствующей буквы"""
    dict_out = {}
    for el in args:
        if dict_out.get(el[0]) == None:
            dict_out.setdefault(el[0],[el])
        else:
            dict_out[el[0]].append(el)
    # результирующий словарь значений
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


