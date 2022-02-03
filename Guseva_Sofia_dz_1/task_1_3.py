#Задание 3. Реализовать склонение слова процент во фразе
#N процентов. Вывести эту фразу на экран отдельной
#строкой для каждого из чисел в интервале от 1 до 100

def transform_string(number: int) -> str:
    #   """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if (number % 10 == 1) and (number != 11):
        string = 'процент'
    elif ((number % 10 == 2) and (number != 12)) or ((number % 10 == 3) and (number != 13)) or ((number % 10 == 4) and (number != 14)):
        string = 'процента'
    else:
        string = 'процентов'
    return f"{number} {string}"

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))