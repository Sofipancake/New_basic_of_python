"""Задание 3
Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:

('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект."""


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ростислав', 'Виктория']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    """генератор, возвращающий
    кортежи
    вида( < tutor >, < klass >)"""
    for name,klass in zip(tutors, klasses):
        yield name,klass


while len(tutors) > len(klasses):
    klasses.append(None)
generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
(next(generator))

#<class 'generator'>
#('Иван', '9А')
#('Анастасия', '7В')
#('Петр', '9Б')
#('Сергей', '9В')
#('Дмитрий', '8Б')
#('Борис', '10А')
#('Елена', '10Б')
#('Ростислав', '9А')
#('Виктория', None)
# Traceback (most recent call last):
#   File "C:\Users\User\PycharmProjects\New_basic_of_python\Guseva_Sofia_dz_5\task_5_3.py", line 39, in <module>
#     (next(generator))
# StopIteration
